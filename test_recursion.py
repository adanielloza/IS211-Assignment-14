import unittest
from recursion import fibonnaci, gcd, compareTo


class TestRecursionFunctions(unittest.TestCase):

    # Fibonacci Tests
    def test_fibonacci_base_cases(self):
        self.assertEqual(fibonnaci(0), 0)
        self.assertEqual(fibonnaci(1), 1)

    def test_fibonacci_general(self):
        self.assertEqual(fibonnaci(5), 5)
        self.assertEqual(fibonnaci(6), 8)
        self.assertEqual(fibonnaci(7), 13)

    def test_fibonacci_invalid(self):
        with self.assertRaises(ValueError):
            fibonnaci(-1)

    # GCD Tests
    def test_gcd_simple(self):
        self.assertEqual(gcd(10, 5), 5)
        self.assertEqual(gcd(15, 3), 3)

    def test_gcd_mixed(self):
        self.assertEqual(gcd(20, 8), 4)
        self.assertEqual(gcd(100, 75), 25)

    # compareTo Tests
    def test_compare_equal(self):
        self.assertEqual(compareTo("abc", "abc"), 0)

    def test_compare_less(self):
        self.assertLess(compareTo("abc", "abd"), 0)
        self.assertLess(compareTo("a", "b"), 0)
        self.assertLess(compareTo("", "abc"), 0)

    def test_compare_greater(self):
        self.assertGreater(compareTo("xyz", "xyb"), 0)
        self.assertGreater(compareTo("b", "a"), 0)
        self.assertGreater(compareTo("abc", ""), 0)


if __name__ == "__main__":
    unittest.main()
