import ast

class ASTAnalyzer(ast.NodeVisitor):
    def _init_(self):
        self.issues = []

    def visit_FunctionDef(self, node):
        if len(node.body) > 20:  # Example heuristic for long functions
            self.issues.append((node.lineno, f"Function '{node.name}' is too long ({len(node.body)} lines)."))
        self.generic_visit(node)

    def visit_For(self, node):
        if isinstance(node.iter, ast.Call) and isinstance(node.iter.func, ast.Name):
            if node.iter.func.id == "range":
                if isinstance(node.iter.args[0], ast.Constant) and node.iter.args[0].value > 1000:
                    self.issues.append((node.lineno, "Loop iterating over more than 1000 items may be inefficient."))
        self.generic_visit(node)

    def visit_While(self, node):
        self.issues.append((node.lineno, "Detected a 'while' loop; ensure it has a termination condition."))
        self.generic_visit(node)

    def analyze(self, code):
        try:
            tree = ast.parse(code)
            self.visit(tree)
            return self.issues
        except SyntaxError as e:
            return [(e.lineno, f"Syntax Error: {e.msg}")]

if __name__ == "_main_":
    sample_code = """
    def example():
        for i in range(2000):
            print(i)
    """
    analyzer = ASTAnalyzer()
    results = analyzer.analyze(sample_code)
    for line, issue in results:
        print(f"Line {line}: {issue}")