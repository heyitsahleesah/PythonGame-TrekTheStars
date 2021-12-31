from unittest import TestCase
from unittest.mock import patch
from game import check_fight_move as check_fight_move
import io


class TestCheckFightMove(TestCase):
    @patch('builtins.input', side_effect=['1', 'm'])
    @patch('random.randrange', side_effect=[70])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_check_fight_move_wrong_input(self, mock_output, mock_random, mock_input):
        enemy = {'Name': "Jem'Hadar", 'HP': 150, 'Attack': 40, 'EXP Earned': 65, 'Weapon': "Kar'takin",
                 'Move': 'stabs'}
        character = {'Name': 'Testy McTesterson', 'Division': 'Medical', 'HP': 100, 'Melee Attack': 150,
                     'Long-Range Attack': 35, 'Level': 1, 'EXP': 0, 'X-Coordinate': 0, 'Y-Coordinate': 0, 'Max HP': 100,
                     'Title': 'Ensign', 'Melee Weapon': 'KaBar Combat Knife', 'Long-Range Weapon': 'type 1 phaser'}
        check_fight_move(character, enemy)
        expected_output = f"The {enemy['Name']} won't wait forever!" \
                          f"\nHow are you going to attack!?" \
                          f"\n[m] \t Melee Attack" \
                          f"\n[l] \t Long-Range Attack"
        game_printed = mock_output.getvalue()
        self.assertIn(expected_output, game_printed)

    @patch('builtins.input', side_effect=['m'])
    @patch('random.randrange', side_effect=[70])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_check_fight_move_melee_output(self, mock_output, mock_random, mock_input):
        enemy = {'Name': "Jem'Hadar", 'Attack': 40, 'EXP Earned': 65, 'Weapon': "Kar'takin", 'HP': 150,
                 'Move': 'stabs'}
        character = {'Name': 'Testy McTesterson', 'EXP': 0, 'Division': 'Medical', 'HP': 100, 'Melee Attack': 150,
                     'Long-Range Attack': 35, 'Level': 1, 'X-Coordinate': 0, 'Y-Coordinate': 0, 'Max HP': 100,
                     'Title': 'Ensign', 'Melee Weapon': 'KaBar Combat Knife', 'Long-Range Weapon': 'type 1 phaser'}
        check_fight_move(character, enemy)
        expected_output = f"\nNice. You swung your {character['Melee Weapon']} at the {enemy['Name']} and did" \
                          f" {character['Melee Attack']} damage."
        game_printed = mock_output.getvalue()
        self.assertIn(expected_output, game_printed)

    @patch('builtins.input', side_effect=['l'])
    @patch('random.randrange', side_effect=[70])
    def test_check_fight_move_long_range_dictionary_change(self, mock_random, mock_input):
        enemy = {'Name': "Jem'Hadar", 'Attack': 40, 'HP': 150, 'EXP Earned': 65, 'Weapon': "Kar'takin",
                 'Move': 'stabs'}
        character = {'Name': 'Testy McTesterson', 'Division': 'Medical', 'HP': 100, 'Melee Attack': 150, 'Level': 1,
                     'Long-Range Attack': 35, 'EXP': 0, 'X-Coordinate': 0, 'Y-Coordinate': 0, 'Max HP': 100,
                     'Title': 'Ensign', 'Melee Weapon': 'KaBar Combat Knife', 'Long-Range Weapon': 'type 1 phaser'}
        check_fight_move(character, enemy)
        expected = {'Name': "Jem'Hadar", 'Attack': 40, 'HP': 0, 'EXP Earned': 65, 'Weapon': "Kar'takin",
                    'Move': 'stabs'}
        self.assertTrue(enemy, expected)
