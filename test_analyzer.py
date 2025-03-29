import unittest
from backend.analysis.ast_analyzer import ASTAnalyzer

class TestASTAnalyzer(unittest.TestCase):
    def test_long_function_detection(self):
        code = """
        def long_function():
            for i in range(25):
                print(i)
        """
        analyzer = ASTAnalyzer()
        results = analyzer.analyze(code)
        self.assertTrue(any("too long" in issue for _, issue in results))

    def test_large_loop_detection(self):
        code = """
        def loop_function():
            for i in range(2000):
                print(i)
        """
        analyzer = ASTAnalyzer()
        results = analyzer.analyze(code)
        self.assertTrue(any("more than 1000 items" in issue for _, issue in results))

    def test_while_loop_warning(self):
        code = """
        def while_loop():
            while True:
                print("Running")
        """
        analyzer = ASTAnalyzer()
        results = analyzer.analyze(code)
        self.assertTrue(any("while' loop" in issue for _, issue in results))

    def test_syntax_error_detection(self):
        code = """
        def broken_code(
            print("Missing parenthesis")
        """
        analyzer = ASTAnalyzer()
        results = analyzer.analyze(code)
        self.assertTrue(any("Syntax Error" in issue for _, issue in results))

if __name__ == "_main_":
    unittest.main()