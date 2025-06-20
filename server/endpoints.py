from fastapi import APIRouter, Body, Query
from server.workflow import  build_test_creation_graph,build_suggest_graph
from server.nodes.run_test_node import run_test_node
from server.temp_store import get_all_test_runs
router = APIRouter()


@router.post("/agent/create_test")
async def agent_create_test(
    test_name: str = Body(...),
    description: str = Body(...),
    run:bool= Body(False)
):
    print("RUN:::", run)
    graph = build_test_creation_graph()
    result = graph.invoke({
        "description": description,
        "test_name": test_name,
        "run": run
    })
    print("result::", result, result.get("state"))
    return result


@router.post("/agent/suggest_test")
async def agent_suggest_test(description: str = Body(..., embed=True)):
    graph = build_suggest_graph()
    result = graph.invoke({"description": description})
    return {"gherkin": result["gherkin"]}

@router.post("/agent/run_test")
async def run_test_from_folder(
    run_id: str = Body(...),
    project_path: str = Body(...)
):
    result = run_test_node({
        "run_id": run_id,
        "project_path": project_path
    })
    return result

@router.get("/get_tests")
async def get_all_tests(test_name: str = Query(default=None)):
    return get_all_test_runs(test_name)

