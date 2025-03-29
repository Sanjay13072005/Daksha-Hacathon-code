from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from backend.ai.optimizer import optimize_code
from backend.ai.scalability_ai import predict_scalability
from backend.analysis.lint_checker import lint_code

app = FastAPI()

class CodeSnippet(BaseModel):
    code: str

@app.post("/optimize")
def optimize(snippet: CodeSnippet):
    """API endpoint to optimize code using AI-powered refactoring."""
    optimized_code = optimize_code(snippet.code)
    return {"optimized_code": optimized_code}

@app.post("/scalability")
def analyze_scalability(snippet: CodeSnippet):
    """API endpoint to analyze code scalability risks."""
    risk_report = predict_scalability(snippet.code)
    return {"scalability_risk": risk_report}

@app.post("/lint")
def lint(snippet: CodeSnippet):
    """API endpoint to check code linting issues."""
    lint_report = lint_code("temp_code.py")  # Assume temporary file usage
    return {"lint_report": lint_report}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)