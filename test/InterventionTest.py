import unittest
from src.entities import intervention

class interventionTest(unittest.TestCase):
    def test_creation_inter(self):
        inter01 = intervention(101, "test", "test")
        self.assertEqual(inter01)


if __name__ == '__main__':
    unittest.main()
