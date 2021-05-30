import unittest
import amazon


class TestMain(unittest.TestCase):

    def test_is_triplet(self):
        self.assertEqual(amazon.is_triplet([1, 2, 3, 4, 5, 6, 7, 8, 9]), True)
        self.assertEqual(amazon.is_triplet([]), False)
        self.assertEqual(amazon.is_triplet([1, 2, 3, 4]), False)
        self.assertEqual(amazon.is_triplet([4, 5, 6]), False)

    def test_find_position_of_multiplication_in_fibonacci(self):
        self.assertEqual(amazon.find_position_of_multiplication_in_fibonacci(1, 3), 6)
        self.assertEqual(amazon.find_position_of_multiplication_in_fibonacci(4, 5), 30)
        with self.assertRaises(ZeroDivisionError):
            amazon.find_position_of_multiplication_in_fibonacci(0, 0)

    def test_find_remainder_of_division(self):
        self.assertEqual(amazon.find_remainder_of_division([1, 28, 76, 78, 98], 9), 3)
        with self.assertRaises(ZeroDivisionError):
            amazon.find_remainder_of_division([], 0)
            amazon.find_remainder_of_division([1, 3, 4, 0], 9)
            amazon.find_remainder_of_division([1, 3, 4, 8], 0)

    def test_first_not_repeated_value(self):
        self.assertEqual(amazon.first_not_repeated_value([1, 28, 76, 78, 98, 28]), 1)
        self.assertEqual(amazon.first_not_repeated_value(["a", "a", "b", 3]), "b")
        self.assertEqual(amazon.first_not_repeated_value([]), [])
        self.assertEqual(amazon.first_not_repeated_value(["a", "b", 3]), "a")
        self.assertEqual(amazon.first_not_repeated_value(["a", "a", "a"]), [])

    def test_search_list_by_substring(self):
        self.assertEqual(amazon.search_list_by_substring(["kalabanga", "palana"], "ka"), ["kalabanga"])
        self.assertEqual(amazon.search_list_by_substring(["pralina", "Dalin", "pralnia"], "pr"), ["pralina", "pralnia"])
        self.assertEqual(amazon.search_list_by_substring([], "kl"), [])
        self.assertEqual(amazon.search_list_by_substring(["hahahha", "kaja", "dolina", "kotlina"], "mal"), [])
        self.assertEqual(amazon.search_list_by_substring(["a", "a", "a"], "m"), [])

    def test_pwd_validation(self):
        self.assertEqual(amazon.pwd_validation("2334Klaara!!"), True)
        self.assertEqual(amazon.pwd_validation(""), False)
        self.assertEqual(amazon.pwd_validation("ajksdgwiadaw"), False)
        self.assertEqual(amazon.pwd_validation("524154653,4"), False)
        self.assertEqual(amazon.pwd_validation("WWWWWWWWWWWW"), False)
        self.assertEqual(amazon.pwd_validation("22ajksdQwiadaw"), True)


if __name__ == '__main__':
    unittest.main()
