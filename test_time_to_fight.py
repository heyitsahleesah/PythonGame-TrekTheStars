from unittest import TestCase
from unittest.mock import patch
import io
from game import time_to_fight as time_to_fight


class Test(TestCase):
    @patch('builtins.input', side_effect=['f', 'm', 'm'])
    @patch('random.randrange', side_effect=[90, 50, 15, 70])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_time_to_fight_enemy_flees(self, mock_output, mock_random, mock_input):
        character = {'Name': 'Testy McTesterson', 'Division': 'Medical', 'HP': 100, 'Melee Attack': 150,
                     'Long-Range Attack': 35, 'Level': 1, 'EXP': 0, 'X-Coordinate': 0, 'Y-Coordinate': 0,
                     'Max HP': 100, 'Title': 'Ensign', 'Melee Weapon': 'KaBar Combat Knife',
                     'Long-Range Weapon': 'type 1 phaser'}
        enemy = {'Name': "Jem'Hadar", 'HP': 150, 'Attack': 40, 'EXP Earned': 65, 'Weapon': "Kar'takin",
                 'Move': 'stabs'}
        time_to_fight(character, enemy)
        expected_output = f"\nLooks like you really scared them, {character['Title']}. They ran away." \
                          f"\nWe're going to have to find them somewhere on the ship though!\n"
        game_printed = mock_output.getvalue()
        self.assertIn(expected_output, game_printed)
