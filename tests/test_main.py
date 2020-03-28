from unittest import TestCase
from main import longest_run


class Test(TestCase):
    # def test_array_not_valid(self):
    #     self.assertEqual(longest_run([1]), None, 'Does not return None on length of arrray < 2')

    def test_array_length2(self):
        self.assertEqual(longest_run([1, 2]), 3, 'Simple array [1, 2]')

    def test_array_increasing(self):
        self.assertEqual(longest_run([1, 2, 1, 3, 4, 5]), 13, 'Monotonically increasing list')

    def test_array_decreasing(self):
        self.assertEqual(longest_run([1, 2, 5, 4, 3, 1]), 13, 'Monotonically decreasing list')

    def test_array_with_repeated_elements(self):
        self.assertEqual(longest_run([1, 2, 5, 4, 4, 3, 2]), 8, 'Array containing repeated elements')

    def test_array_example_1(self):
        self.assertEqual(longest_run([1, 2, 3, 2, 1]), 6, 'Lists of equal length and content')

    def test_array_example_2(self):
        self.assertEqual(longest_run([1, 2, 3, 2, -1]), 6, 'List of equal length but different content')

    def test_array_example_3(self):
        self.assertEqual(longest_run([1, 2, 3, 4, 5, 6, 7, 8, 9]), 45, 'Pure monotonically increasing list')

    def test_array_example_3(self):
        self.assertEqual(longest_run([9, 8, 7, 6, 5, 4, 3, 2, 1]), 45, 'Pure monotonically decreasing list')