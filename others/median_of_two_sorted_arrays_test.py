from median_of_two_sorted_arrays import Solution
import unittest


class TestCase(unittest.TestCase):
    def test_empty(self):
        sol = Solution()
        self.assertEqual(sol.findMedianSortedArrays([], [0]), 0)
        self.assertEqual(sol.findMedianSortedArrays([0], []), 0)
        with self.assertRaises(ValueError):
            sol.findMedianSortedArrays([], [])

    def test_even(self):
        sol = Solution()
        self.assertAlmostEqual(sol.findMedianSortedArrays([0], [1, 2, 3]), 1.5)
        self.assertAlmostEqual(sol.findMedianSortedArrays([0, 1], [2, 3]), 1.5)

    def test_odd(self):
        sol = Solution()
        self.assertEqual(sol.findMedianSortedArrays([0], [2, 3]), 2)
        self.assertEqual(sol.findMedianSortedArrays([0, 1], [3]), 1)

    def test_sizediff(self):
        sol = Solution()
        a = [num for num in range(2, 101)]
        b = [1]
        self.assertAlmostEqual(sol.findMedianSortedArrays(a, b), 50.5)
        self.assertAlmostEqual(sol.findMedianSortedArrays(b, a), 50.5)


if __name__ == "__main__":
    unittest.main()
