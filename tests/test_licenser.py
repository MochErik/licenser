import unittest
from licenser.cli import generate_license

class TestLicenser(unittest.TestCase):
    def test_mit_gen(self):
        text = generate_license("mit", "Test User", 2026)
        self.assertIn("MIT License", text)
        self.assertIn("Test User", text)
if __name__ == "__main__": unittest.main()
