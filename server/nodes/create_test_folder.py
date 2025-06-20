from datetime import datetime
from pathlib import Path
from server.temp_store import add_test_run

BASE_PATH = Path("tests_storage")

def create_test_folder_func(state: dict) -> dict:
    test_name = state["test_name"]
    gherkin_code = state["gherkin"]

    timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    run_id = f"{test_name}"
    project_path = BASE_PATH / run_id

    # Create Hercules-compatible folder structure
    (project_path / "gherkin_files").mkdir(parents=True,exist_ok=True)
    (project_path / "output").mkdir(exist_ok=True)
    (project_path / "test_data").mkdir(exist_ok=True)
    (project_path / "proofs").mkdir(exist_ok=True)

    # Save Gherkin file
    feature_path = project_path / "gherkin_files" / "test.feature"
    feature_path.write_text(gherkin_code)
    add_test_run(test_name, run_id, project_path)
    # Return updated state
    print("project_path::", str(project_path), state)
    return {
        **state,
        "run_id": run_id,
        "project_path": str(project_path),
        "status": None
    }
