from unittest import TestCase
from unittest.mock import patch
from game import introduction as introduction
import io


class TestIntroduction(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_introduction(self, mock_output):
        character = {'Name': 'Testy McTesterson', 'Title': 'Ensign'}
        introduction(character)
        expected_output = f"\n\n...What was that!?"
        game_printed = mock_output.getvalue()
        self.assertIn(expected_output, game_printed)

    def test_introduction_dictionary_unchanged(self):
        character = {'Name': 'Testy McTesterson', 'Title': 'Ensign'}
        introduction(character)
        self.assertTrue(character, {'Name': 'Testy McTesterson', 'Title': 'Ensign'})