from unittest import TestCase
from unittest.mock import patch
from game import check_for_enemy as check_for_enemy


class TestCheckForEnemy(TestCase):
    @patch('random.randrange', return_value=5)
    def test_check_for_enemy_true(self, mock_random):
        expected = True
        actual = check_for_enemy()
        self.assertEqual(actual, expected)

    @patch('random.randrange', return_value=19)
    def test_check_for_enemy_true_upper(self, mock_random):
        expected = True
        actual = check_for_enemy()
        self.assertEqual(actual, expected)

    @patch('random.randrange', return_value=20)
    def test_check_for_enemy_false(self, mock_random):
        expected = False
        actual = check_for_enemy()
        self.assertEqual(actual, expected)
