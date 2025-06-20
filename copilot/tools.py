from mcp.server.fastmcp import FastMCP
import requests

mcp = FastMCP(name="tester") # Math is just a name for server

@mcp.tool()
def suggest_test(description:str)->str:
    """Suggests a Gherkin test case based on a user-provided natural language description.
      Args:
        description (string): _description_
          Returns:
       f"Gherkin (string) : _description_
    """
    res = requests.post(
    "http://localhost:8000/agent/suggest_test",
    json={"description": description}
)
    print("res.json()",res.json() )
    return res.json().get("gherkin", "No Gherkin generated.")

@mcp.tool()
def create_test(test_name: str, description: str, run: bool = False) -> str:
    """Creates and optionally runs a test case from name + description.
    Args:
        test_name (string): _description_
        description (string): _description_
        run (boolean): _description_
       
    Returns:
       "Gherkin:\n{data.get('gherkin')}\n\nStatus: {data.get('status')}" (string) : _description_
    """
    print("create test with::: ", test_name, run)
    res = requests.post(
        "http://localhost:8000/agent/create_test",
        json={
            "test_name": test_name,
            "description": description,
            "run": run
        }
    )
    data = res.json()
    print("create:::data", data)
    return f"Gherkin:\n{data.get('gherkin')}\n\nStatus: {data.get('status')}"

# @mcp.tool()
# def run_test(run_id: str, project_path: str) -> str:
#     """if project_path and run_id is given, Runs a test 
#         Args:
#         run_id (string): _description_
#         project_path (string): _description_
       
#     Returns:
#       "Status: {data.get('status')}, Report: {data.get('html_report')}"(string) : _description_
#     """
#     print("run test:::")
#     res = requests.post(
#         "http://localhost:8000/agent/run_test",
#         json={
#             "run_id": run_id,
#             "project_path": project_path
#         }
#     )
#     data = res.json()
#     print("data:::run test", data)
#     return  f"Status: {data.get('status')}, Report: {data.get('html_report')}"

if __name__ == "__main__":
    mcp.run(transport="stdio")
