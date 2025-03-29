import unittest
from backend.ai.optimizer import CodeOptimizer

class TestCodeOptimizer(unittest.TestCase):
    def setUp(self):
        self.optimizer = CodeOptimizer()
    
    def test_redundant_code_removal(self):
        code = """
        def example():
            x = 5
            x = 5  # Redundant assignment
            return x
        """
        optimized_code = self.optimizer.optimize(code)
        self.assertNotIn("x = 5  # Redundant assignment", optimized_code)
    
    def test_loop_unrolling(self):
        code = """
        def loop_example():
            for i in range(3):
                print(i)
        """
        optimized_code = self.optimizer.optimize(code)
        self.assertIn("print(0)", optimized_code)
        self.assertIn("print(1)", optimized_code)
        self.assertIn("print(2)", optimized_code)
    
    def test_dead_code_elimination(self):
        code = """
        def dead_code():
            return 42
            x = 100  # Unreachable code
        """
        optimized_code = self.optimizer.optimize(code)
        self.assertNotIn("x = 100", optimized_code)
    
    def test_variable_renaming(self):
        code = """
        def rename_vars():
            very_long_variable_name = 10
            return very_long_variable_name
        """
        optimized_code = self.optimizer.optimize(code)
        self.assertNotIn("very_long_variable_name", optimized_code)
    
if __name__ == "_main_":
    unittest.main()