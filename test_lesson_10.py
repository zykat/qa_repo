import unittest
#
#
# class TestMyCode(unittest.TestCase):
#
#     def setUp(self) -> None:
#         print("Starting testing...")
#         print("Set data or something")
#
#     def test_is_a_greater_than_b(self):
#         print("test_is_a_greater_than_b")
#         a = 4
#         b = 3
#         self.assertTrue(a > b,f"{a} is not greater than {b}")
#
#     def test_x_is_equal_to_y(self):
#         print("test_x_is_equal_to_y")
#         x = 45
#         y = 45
#         self.assertTrue(x == y, f"{x} is not equal to {y}")
#         # Or
#         # self.assertEqual(x,y)
#
#     def tearDown(self) -> None:
#         print("Clearing data or something")
#         print("Testing is done!")
#
#
# if __name__ == '__main__':
#     unittest.main()

import unittest
from modules.utils import reverse_string_slicing

class testStrUtilsSlicing(unittest.TestCase):

    def test_reverse_string_slicing_lower_case(self):
        self.assertEqual(reverse_string_slicing("some"), "emos")

    def test_reverse_string_slicing_upper_case(self):
        self.assertEqual(reverse_string_slicing("SOME"), "EMOS")

    def test_reverse_string_slicing_capitalised(self):
        self.assertEqual(reverse_string_slicing("Some"), "emoS")

    def test_reverse_string_slicing_number(self):
        self.assertEqual(reverse_string_slicing("456"), "654", "wrong output")

    def test_reverse_string_slicing_capitalised(self):
        self.assertEqual(reverse_string_slicing(" "), " ")

    def test_negative_reverse_string_boolean(self):
        self.assertRaises(TypeError, reverse_string_slicing, True)