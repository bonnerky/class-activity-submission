import unittest
import fib

class Testfib(unittest.TestCase):
    def test_fib(self):
        self.assertEqual(fib.fib(3), 2)
        self.assertEqual(fib.fib(0), 0)
        self.assertEqual(fib.fib(5), 5)


if __name__ == '__main__':
    unittest.main(verbosity=2)