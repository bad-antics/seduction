import unittest,sys,os
sys.path.insert(0,os.path.join(os.path.dirname(__file__),"..","src"))
from seduction.core import SeductionEngine

class TestSeduction(unittest.TestCase):
    def test_form(self):
        s=SeductionEngine()
        r=s.analyze_form("ritual")
        self.assertIn("principle",r)
    def test_contrast(self):
        s=SeductionEngine()
        r=s.seduction_vs_production()
        self.assertIn("seduction",r)
        self.assertIn("production",r)
    def test_insight(self):
        s=SeductionEngine()
        self.assertIsInstance(s.generate_insight(),str)

if __name__=="__main__": unittest.main()
