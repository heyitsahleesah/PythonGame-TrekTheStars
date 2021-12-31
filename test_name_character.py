from unittest import TestCase
from unittest.mock import patch
from game import name_character as name_character


class TestNameCharacter(TestCase):
    @patch('builtins.input', return_value='Testy McTesterson')
    def test_name_character_dictionary_changed(self, mock_input):
        expected = {'Name': 'Testy McTesterson', 'Title': 'Ensign'}
        actual = name_character()
        self.assertEqual(actual, expected)
