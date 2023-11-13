"""test_cold.py
"""

import unittest
from cold import answer


class TestCold(unittest.TestCase):
    """test class
    """
    def test_answer(self) -> None:
        """tests cold.py
        """
        data = "-3 -454 0 454 -565656 -45445"
        ans = answer(data)
        expected = 4
        self.assertEqual(ans, expected)

    def test_answer1(self) -> None:
        """tests answer 1 given by kattis
        """
        self.assertEqual(answer("23 32 6 566 7757"), 0)
