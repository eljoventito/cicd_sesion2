import unittest
from my_app.my_app_v1 import add

class TestMain(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1,2), 3)
        self.assertEqual(add(-1,1), 0)
        self.assertEqual(add(1,2), 3)

if __name__ == '__main__':
    unittest.main()