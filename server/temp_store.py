
test_runs = []

def add_test_run(test_name:str,run_id: str, project_path: str,):
    test_runs.append({
        "run_id": run_id,
        "project_path": project_path,
        "test_name": test_name
    })

def get_all_test_runs(test_name: str = None):
    if not test_name:
        return test_runs
    return [
        run for run in test_runs
        if test_name.lower() in run["test_name"].lower()
    ]