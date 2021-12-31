from unittest import TestCase
from unittest.mock import patch
from game import character_death as character_death
import io


class TestCharacterDeath(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_character_death(self, mock_output):
        with self.assertRaises(SystemExit) as dead:
            character = {'Name': 'Testy McTesterson', 'Title': 'Ensign'}
            character_death(character)
            actual = mock_output.getvalue()
            expected = "\n'Death is that state in which one exists only in the memory of others..."
            exit_message = dead.exception
            self.assertTrue(expected in actual)
            self.assertEquals(exit_message, 0)

    def test_character_death_dictionary_unchanged(self):
        with self.assertRaises(SystemExit) as end:
            character = {'Name': 'Testy McTesterson', 'Title': 'Ensign'}
            actual = character_death(character)
            expected = {'Name': 'Testy McTesterson', 'Title': 'Ensign'}
            self.assertEquals(expected, actual)
