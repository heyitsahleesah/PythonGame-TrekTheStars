from unittest import TestCase
from game import class_information as class_information
from unittest.mock import patch
import io


class TestClassInformation(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_class_information_medical(self, mock_output):
        character = {'Name': 'Testy McTesterson', 'Title': 'Ensign'}
        class_information(character, '1')
        expected_output = "\nyou are able to provide a bit better healing for yourself if there is any ruckus."
        game_printed = mock_output.getvalue()
        self.assertTrue(expected_output in game_printed)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_class_information_engineering(self, mock_output):
        character = {'Name': 'Testy McTesterson', 'Title': 'Ensign'}
        class_information(character, '2')
        expected_output = "\nYou're job is to maintain the ship's functionality. This can include "\
                          "\nmaintaining/improving the warp drive and maintaining the ship's database, "\
                          "\ncircuitry, and processors."
        game_printed = mock_output.getvalue()
        self.assertTrue(expected_output in game_printed)

    def test_class_information_dictionary_unchanged(self):
        character = {'Name': 'Testy McTesterson', 'Title': 'Ensign'}
        class_information(character, '2')
        self.assertTrue(character, {'Name': 'Testy McTesterson', 'Title': 'Ensign'})
