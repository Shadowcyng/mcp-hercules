from langgraph.prebuilt import create_react_agent
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import initialize_agent, AgentType
import asyncio
import os

load_dotenv(".env")
async def main():
    try:
        default_project_path = os.path.abspath("tests_storage/test")  # Default path for test files
        client = MultiServerMCPClient(
            {
                "tester": {
                    "command": "python",
                    "args": [os.path.abspath("copilot/tools.py")],
                    "transport": "stdio",
                },
            }
        )
        os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
        if not os.environ["GROQ_API_KEY"]:
            raise ValueError("GROQ_API_KEY not set in .env")
        tools = await client.get_tools()
        llmModel = os.getenv("MODEL")
        if not llmModel:
            raise ValueError("MODEL not set in .env")
        model = ChatGroq(model=llmModel, temperature=0.1, max_retries=1)
        model = model.bind_tools(tools, tool_choice="auto")
        agent = create_react_agent(model, tools)
        print("Tools:", [tool.name for tool in tools])

        while True:
            user_input = input("🧑 You: ")
            if user_input.strip().lower() in {"exit", "quit", "goodby", "bye", ""}:
                print("👋 Goodbye.")
                break
            print("user", user_input)
            messages = [
                {
                    "role": "system",
                    "content": (
                        "You are an assistant that generates and runs Gherkin test cases using the 'suggest_test' and 'create_test' tools. "
                        "Based on the user input, select the appropriate tool: "
                        "- Use 'suggest_test' to suggest a test case when the user asks for a test case suggestion (e.g., 'suggest a test for...'). "
                        "- Use 'create_test' to create a test case when the user specifies a test name or asks to create a test (e.g., 'create test named...'). and run if mentioned"
                        "If the user requests multiple actions (e.g., create and run), call the tools sequentially. "
                        "Only call one tool per input and stop after that. Never call a tool more than once."
                        "default_project_path= '{}'"
                        "Respond with structured JSON tool calls only."
                        "for one prompt only run one tool. for suggestion dont run create and vice versa"
                    ).format(default_project_path)
                },
                {"role": "user", "content": user_input},
            ]
            result = await agent.ainvoke({"messages": messages})
            print("Raw result:", result)

            messages = result.get("messages", [])
            output = []
            tool_called = False
            for message in messages:
                print(f"Processing message: {message}")
                if hasattr(message, "tool_calls") and message.tool_calls:
                    print("Tool calls detected:", message.tool_calls)
                    tool_called = True
                elif hasattr(message, "content") and message.content and hasattr(message, "name") and message.name in ["suggest_test", "create_test"]:
                    if message.content and message.content != "None":
                        output.append(f"{message.name} output:\n{message.content}")
                        tool_called = True
                elif hasattr(message, "content") and message.content and not tool_called:
                    output.append(f"Assistant: {message.content}")

            if not tool_called:
                print("Warning: No tool calls detected in response")
            print("\n🤖 Copilot:\n" + "\n\n".join(output) if output else "[No output]" + "\n")

    except Exception as e:
        print("error:", e)

asyncio.run(main())