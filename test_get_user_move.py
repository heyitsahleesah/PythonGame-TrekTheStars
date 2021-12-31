import io
from unittest import TestCase
from unittest.mock import patch
from game import get_user_move as get_user_move


class TestGetUserMove(TestCase):
    @patch('builtins.input', return_value='1')
    def test_get_user_move_one(self, mock_input):
        character = {'Name': 'Testy McTesterson', 'Title': 'Ensign'}
        expected = '1'
        actual = get_user_move(character)
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value='2')
    def test_get_user_move_two(self, mock_input):
        character = {'Name': 'Testy McTesterson', 'Title': 'Ensign'}
        expected = '2'
        actual = get_user_move(character)
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value='3')
    def test_get_user_move_three(self, mock_input):
        character = {'Name': 'Testy McTesterson', 'Title': 'Ensign'}
        expected = '3'
        actual = get_user_move(character)
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value='4')
    def test_get_user_move_four(self, mock_input):
        character = {'Name': 'Testy McTesterson', 'Title': 'Ensign'}
        expected = '4'
        actual = get_user_move(character)
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['l', '4'])
    def test_get_user_move_wrong_input(self, mock_input):
        character = {'Name': 'Testy McTesterson', 'Title': 'Ensign'}
        expected = '4'
        actual = get_user_move(character)
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['l', '6', '4'])
    def test_get_user_move_multiple_wrong_input(self, mock_input):
        character = {'Name': 'Testy McTesterson', 'Title': 'Ensign'}
        expected = '4'
        actual = get_user_move(character)
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value='Q')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_user_move_quit_uppercase(self, mock_output, mock_input):
        with self.assertRaises(SystemExit) as end_game_upper_q:
            character = {'Name': 'Testy McTesterson', 'Title': 'Ensign'}
            get_user_move(character)
            actual = mock_output.getvalue()
            expected = f"Thanks for playing, {character['Title']}{character['Name']}!  \nLive long and Prosper."
            exit_message = end_game_upper_q.exception
            self.assertTrue(expected in actual)
            self.assertEquals(exit_message, 0)

    @patch('builtins.input', return_value='q')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_user_move_quit_lowercase(self, mock_output, mock_input):
        with self.assertRaises(SystemExit) as end_game_lower_q:
            character = {'Name': 'Testy McTesterson', 'Title': 'Ensign'}
            get_user_move(character)
            actual = mock_output.getvalue()
            expected = f"Thanks for playing, {character['Title']}{character['Name']}!  \nLive long and Prosper."
            exit_message = end_game_lower_q.exception
            self.assertTrue(expected in actual)
            self.assertEquals(exit_message, 0)

    @patch('builtins.input', return_value='4')
    def test_get_user_move_character_dictionary_unchanged(self, mock_input):
        character = {'Name': 'Testy McTesterson', 'Title': 'Ensign'}
        get_user_move(character)
        self.assertTrue(character, {'Name': 'Testy McTesterson', 'Title': 'Ensign'})
