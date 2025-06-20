from langgraph.graph import StateGraph, END
from server.agents.test_case_generator import test_case_generator_agent
from server.nodes.create_test_folder import create_test_folder_func
from server.nodes.run_test_node import run_test_node

# Optional: define types for clarity
class TestState(dict):
    description: str
    test_name: str
    gherkin: str | None
    run_id: str | None
    project_path: str | None
    status:str | None

# LangGraph-compatible wrapper
def generate_gherkin_node(state: TestState) -> TestState:
    result = test_case_generator_agent({"description": state["description"]})
    return {**state, "gherkin": result["gherkin"]}


def build_suggest_graph():
    builder = StateGraph(TestState)
    builder.add_node("GenerateGherkin", generate_gherkin_node)
    builder.set_entry_point("GenerateGherkin")
    builder.set_finish_point("GenerateGherkin")
    graph = builder.compile()
    # img = ((graph.get_graph().draw_mermaid_png()))
    # with open("suggestion_graph.png", "wb") as f:
    #     f.write(img)
    
    return graph

def should_run_test(state:TestState):
    return "RunTest" if state.get("run", True) else "END"

def build_test_creation_graph():
    builder = StateGraph(TestState)
    # Add nodes
    builder.add_node("GenerateGherkin", generate_gherkin_node)
    builder.add_node("CreateTestFolder", create_test_folder_func)
    builder.add_node("RunTest", run_test_node)

    # Wire nodes together
    builder.set_entry_point("GenerateGherkin")
    builder.add_edge("GenerateGherkin", "CreateTestFolder")
    builder.add_conditional_edges("CreateTestFolder",
        should_run_test,
        path_map={
            "RunTest": "RunTest",
            "END": END
        })

    builder.add_edge("RunTest",END)

    graph = builder.compile()
    # img = ((graph.get_graph().draw_mermaid_png()))
    # with open("creation_run_graph.png", "wb") as f:
    #     f.write(img)
    return graph

