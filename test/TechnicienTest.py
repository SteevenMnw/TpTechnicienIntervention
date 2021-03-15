import unittest
from src.entities import technicien

class TechnicienTest(unittest.TestCase):
    def test_creation_tech(self):
        tech01 = technicien("Jean", "Test")
        self.assertIsNone(tech01)


if __name__ == '__main__':
    unittest.main()
