from unittest import TestCase
from unittest.mock import patch
from game import end_game as end_game
import io


class TestEndGame(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_end_game(self, mock_output):
        with self.assertRaises(SystemExit) as end:
            character = {'Name': 'Testy McTesterson', 'Title': 'Ensign'}
            end_game(character)
            actual = mock_output.getvalue()
            expected = f"Thanks for playing, {character['Title']}{character['Name']}!  \nLive long and Prosper."
            exit_message = end.exception
            self.assertTrue(expected in actual)
            self.assertEquals(exit_message, 0)

    def test_end_game_dictionary_unchanged(self):
        with self.assertRaises(SystemExit) as end:
            character = {'Name': 'Testy McTesterson', 'Title': 'Ensign'}
            expected = {'Name': 'Testy McTesterson', 'Title': 'Ensign'}
            self.assertEquals(expected, end_game(character))
