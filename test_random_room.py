from unittest import TestCase
from unittest.mock import patch
from game import random_room as random_room


class TestRandomRoom(TestCase):
    @patch('random.randint', return_value=3)
    def test_random_room(self, mock_random):
        expected = 'Main Engineering'
        actual = random_room()
        self.assertEqual(actual, expected)

    @patch('random.randint', return_value=0)
    def test_another_random_room(self, mock_random):
        expected = 'The Bridge'
        actual = random_room()
        self.assertEqual(actual, expected)
