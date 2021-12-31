from unittest import TestCase
from unittest.mock import patch
import io
from game import fight_or_flee as fight_or_flee


class TestFightOrFlee(TestCase):
    @patch('builtins.input', return_value='r')
    @patch('random.randrange', return_value=20)
    def test_fight_or_flee_success(self, mock_random, mock_input):
        character = {'Name': 'Testy McTesterson', 'HP': 100, 'Title': 'Ensign'}
        enemy = {'Name': "Jem'Hadar", 'HP': 150, 'Attack': 40, 'EXP Earned': 65, 'Weapon': "Kar'takin",
                 'Move': 'stabs'}
        expected = True
        actual = fight_or_flee(character, enemy)
        self.assertEqual(actual, expected)

    @patch('builtins.input', return_value='r')
    @patch('random.randrange', return_value=15)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_fight_or_flee_damage_message(self, mock_output, mock_random, mock_input):
        character = {'Name': 'Testy McTesterson', 'HP': 100, 'Title': 'Ensign'}
        enemy = {'Name': "Jem'Hadar", 'HP': 150, 'Attack': 40, 'EXP Earned': 65, 'Weapon': "Kar'takin",
                 'Move': 'stabs'}
        fight_or_flee(character, enemy)
        expected_output = f"\nYou tripped as you ran and the {enemy['Name']} smacks you,"
        f"doing {enemy['Attack'] / 2} damage!"
        game_printed = mock_output.getvalue()
        self.assertIn(expected_output, game_printed)

    @patch('builtins.input', return_value='f')
    def test_fight_or_flee_fight(self, mock_input):
        character = {'Name': 'Testy McTesterson', 'HP': 100, 'Title': 'Ensign'}
        enemy = {'Name': "Jem'Hadar", 'HP': 150, 'Attack': 40, 'EXP Earned': 65, 'Weapon': "Kar'takin",
                 'Move': 'stabs'}
        expected = False
        actual = fight_or_flee(character, enemy)
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=['d', 'f'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_fight_or_flee_wrong_output(self, mock_output, mock_input):
        character = {'Name': 'Testy McTesterson', 'HP': 100, 'Title': 'Ensign'}
        enemy = {'Name': "Jem'Hadar", 'HP': 150, 'Attack': 40, 'EXP Earned': 65, 'Weapon': "Kar'takin",
                 'Move': 'stabs'}
        fight_or_flee(character, enemy)
        expected_output = f"\n{character['Title']} {character['Name']}! The enemy looks strong!" \
                          f"\nDo you want to stay and fight [f] or will you flee [r]?"\
                          f"\nStarfleet won't judge you!"\
                          f"\n"
        game_printed = mock_output.getvalue()
        self.assertIn(expected_output, game_printed)

    @patch('builtins.input', side_effect=['8', 'd', 'f'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_fight_or_flee_multiple_wrong_output(self, mock_output, mock_input):
        enemy = {'Name': "Jem'Hadar", 'HP': 150, 'Attack': 40, 'EXP Earned': 65, 'Weapon': "Kar'takin",
                 'Move': 'stabs'}
        character = {'Name': 'Testy McTesterson', 'HP': 100, 'Title': 'Ensign'}
        fight_or_flee(character, enemy)
        expected_output = f"\n{character['Title']} {character['Name']}! The enemy looks strong!"\
                          f"\nDo you want to stay and fight [f] or will you flee [r]?"\
                          f"\nStarfleet won't judge you!"\
                          f"\n"
        game_printed = mock_output.getvalue()
        self.assertIn(expected_output, game_printed)
