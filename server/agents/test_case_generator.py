from typing import TypedDict
from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage # Import SystemMessage

load_dotenv()

class Input(TypedDict):
    description: str

class Output(TypedDict):
    gherkin: str

print(os.getenv("GROQ_API_KEY"))

os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")
os.environ["MODEL"]=os.getenv("MODEL")

# LLM client using LangChain ChatGroq
llm = ChatGroq(
    model=os.environ["MODEL"], 
)

def test_case_generator_agent(input: Input) -> Output:
    prompt = f"""
You are an expert QA automation engineer.

Convert the following test case description into a valid Gherkin `.feature` file.
Respond only with the Gherkin code.

Description:
\"\"\"
{input['description']}
\"\"\"
"""

    response = llm([SystemMessage(content=prompt)])
    print("response from llm for g code::::", response)
    return {"gherkin": response.content.strip()}
