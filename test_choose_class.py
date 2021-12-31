from unittest import TestCase
from game import choose_class as choose_class
from unittest.mock import patch
import io


class TestChooseClass(TestCase):
    @patch('builtins.input', return_value='1')
    def test_choose_class(self, mock_input):
        expected = {'Division': 'Medical', 'HP': 100, 'Melee Attack': 30, 'Long-Range Attack': 35,
                    'Long-Range Weapon': 'type 1 phaser', 'Melee Weapon': 'KaBar Combat Knife'}
        actual = choose_class()
        self.assertEqual(actual, expected)

    @patch('builtins.input', return_value='1')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_choose_class_output(self, mock_output, mock_input):
        choose_class()
        game_printed = mock_output.getvalue()
        expected_output = "Welcome to Medical! Happy to have you!"
        self.assertIn(expected_output, game_printed)

    @patch('builtins.input', side_effect=['p', '2'])
    def test_choose_class_wrong_input(self, mock_input):
        expected = {'Division': 'Engineering', 'HP': 75, 'Melee Attack': 30, 'Long-Range Attack': 35,
                    'Long-Range Weapon': 'type 3 phaser rifle', 'Melee Weapon': 'KaBar Combat Knife'}
        actual = choose_class()
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=['p', '9', '3'])
    def test_choose_class_multiple_wrong_input(self, mock_input):
        expected = {'Division': 'Command', 'HP': 75, 'Melee Attack': 40, 'Long-Range Attack': 35,
                    'Long-Range Weapon': 'type 2 phaser pistol', 'Melee Weapon': 'KaBar Combat Knife'}
        actual = choose_class()
        self.assertEqual(actual, expected)
