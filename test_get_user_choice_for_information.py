from unittest import TestCase
from unittest.mock import patch
import io
from game import get_user_choice_for_information as get_user_choice_for_information


class TestUserChoiceForInfo(TestCase):
    @patch('builtins.input', return_value='s')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_user_choice_for_information_skipped(self, mock_output, mock_input):
        character = {'Name': 'Testy McTesterson', 'Title': 'Ensign'}
        get_user_choice_for_information(character)
        game_printed = mock_output.getvalue()
        expected_output = f"Looks like you know all this already, {character['Title']} {character['Name']}! Awesome!"
        self.assertTrue(expected_output in game_printed)

    @patch('builtins.input', return_value='s')
    def test_get_user_choice_for_information_dictionary_unchanged(self, mock_input):
        character = {'Name': 'Testy McTesterson', 'Title': 'Ensign'}
        get_user_choice_for_information(character)
        self.assertTrue(character, {'Name': 'Testy McTesterson', 'Title': 'Ensign'})
