#!/usr/bin/python3
"""import unittest for base.py."""

class BaseTestCase(unittest.TestCase):

    def setUp(self):
        # Set up any required test data or resources
        self.data = [1, 2, 3, 4, 5]

    def tearDown(self):
        # Tear down any resources used by the test
        self.data = None

    def test_data_length(self):
        # Test the length of the data
        self.assertEqual(len(self.data), 5)

    def test_data_contains_value(self):
        # Test if a specific value is present in the data
        self.assertIn(3, self.data)

    def test_data_type(self):
        # Test the type of the data
        self.assertIsInstance(self.data, list)

    def test_data_sum(self):
        # Test the sum of the data
        self.assertEqual(sum(self.data), 15)

    def test_data_max(self):
        # Test the maximum value in the data
        self.assertEqual(max(self.data), 5)

if __name__ == '__main__':
    unittest.main()

