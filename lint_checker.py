import subprocess

def lint_code(file_path):
    """Runs a linter (pylint) on the given Python file and returns linting results."""
    try:
        result = subprocess.run(["pylint", file_path], capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return f"Error running linter: {str(e)}"

if __name__ == "_main_":
    sample_file = "example.py"
    lint_results = lint_code(sample_file)
    print("Linting Results:\n", lint_results)