import subprocess
from pathlib import Path
import os
import random
def run_test_node(state: dict) -> dict:
    project_path = Path(state["project_path"])
    run_id = state["run_id"]
    llm_model = os.getenv("MODEL")
    llm_api_key = os.getenv("GROQ_API_KEY")
    # if not llm_api_key:
    #     return {**state, "status": "error", "error": "Missing LLM API key"}

    try:
        print(f"[RunTestNode] Running test for {run_id}")

        input_file = project_path / "gherkin_files" / "test.feature"
        output_path = project_path / "output"
        test_data_path = project_path / "test_data"
        print("input_file::", input_file)
        # result = subprocess.run(
        #     [
        #         "testzeus-hercules",
        #         "--input-file", str(input_file),
        #         "--output-path", str(output_path),
        #         "--test-data-path", str(test_data_path),
        #         "--llm-model", llm_model,
        #         "--llm-model-api-key", llm_api_key
        #     ],
        #     capture_output=True,
        #     text=True,
        #     check=False,
        # )

        # commented because I do not have open ai paid plan to run hercules
        # mock
        html_report = output_path / "test.feature_result.html"
        junit_report = output_path / "test.feature_result.xml"
        # status = "passed" if result.returncode == 0 else "failed"
        status = "passed" if random.Random().randint(0,1) > .5 else "failed"
        html_report.write_text(f"<html><body><h1>{state.get("test_name", "Fake")}: {status}</h1></body></html>")
        junit_report.write_text(f"<testsuite><testcase name='{state.get("test_name", "Fake")}'/></testsuite>")

        return {
            **state,
            "status": status,
            "html_report": str(html_report),
            "junit_report": str(junit_report),
            "error":None
            # "error": result.stderr if result.returncode != 0 else None
        }

    except Exception as e:
        return {
            **state,
            "status": "error",
            "error": str(e)
        }
