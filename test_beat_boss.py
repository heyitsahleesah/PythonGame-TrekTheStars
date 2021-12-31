from unittest import TestCase
from unittest.mock import patch
from game import beat_boss as beat_boss
import io


class TestBeatBoss(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_beat_boss(self, mock_output):
        with self.assertRaises(SystemExit) as end:
            character = {'Name': 'Testy McTesterson', 'Title': 'Ensign'}
            beat_boss(character)
            actual = mock_output.getvalue()
            expected = "\nHeghlu’meH QaQ jajvam!"
            exit_message = end.exception
            self.assertTrue(expected in actual)
            self.assertEquals(exit_message, 0)

    def test_beat_boss_dictionary_unchanged(self):
        with self.assertRaises(SystemExit) as end:
            character = {'Name': 'Testy McTesterson', 'Title': 'Ensign'}
            actual = beat_boss(character)
            expected = {'Name': 'Testy McTesterson', 'Title': 'Ensign'}
            self.assertEquals(expected, actual)
