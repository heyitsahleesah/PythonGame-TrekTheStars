from unittest import TestCase
from unittest.mock import patch
from game import boss_battle as boss_battle
import io


class TestBossBattle(TestCase):
    @patch('builtins.input', side_effect=['m'])
    @patch('random.randrange', side_effect=[70])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_boss_battle_win_output(self, mock_output, mock_random, mock_input):
        with self.assertRaises(SystemExit) as end:
            character = {'Name': 'Testy McTesterson', 'HP': 100, 'Melee Attack': 150,
                         'Long-Range Attack': 35, 'Level': 1, 'EXP': 0, 'X-Coordinate': 0, 'Y-Coordinate': 0,
                         'Max HP': 100, 'Title': 'Ensign', 'Division': 'Medical',
                         'Melee Weapon': 'KaBar Combat Knife', 'Long-Range Weapon': 'type 1 phaser'}
            boss = {'Name': "Jem'Hadar", 'HP': 150, 'Attack': 40, 'EXP Earned': 65, 'Weapon': "Kar'takin",
                    'Move': 'stabs'}
            boss_battle(character, boss)
            expected_output = f"\nYou killed the {boss['Name']}!" \
                              f"\nYou win all the fame and glory, {character['Title']} {character['Name']}"
            game_printed = mock_output.getvalue()
            self.assertIn(expected_output, game_printed)

    @patch('builtins.input', side_effect=['m'])
    @patch('random.randrange', side_effect=[70])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_boss_battle_output(self, mock_output, mock_random, mock_input):
        with self.assertRaises(SystemExit) as end:
            character = {'Name': 'Testy McTesterson', 'Division': 'Medical', 'HP': 100, 'Melee Attack': 150,
                         'Long-Range Attack': 35, 'Level': 1, 'Max HP': 100, 'EXP': 0, 'X-Coordinate': 0,
                         'Y-Coordinate': 0, 'Title': 'Ensign',
                         'Melee Weapon': 'KaBar Combat Knife', 'Long-Range Weapon': 'type 1 phaser'}
            boss = {'Name': "Jem'Hadar", 'HP': 150, 'Attack': 40, 'EXP Earned': 65, 'Weapon': "Kar'takin",
                    'Move': 'stabs'}
            boss_battle(character, boss)
            expected_output = f"\nYour health: {character['HP']}" \
                              f"\nBoss health: {boss['HP']}\n"
            game_printed = mock_output.getvalue()
            self.assertIn(expected_output, game_printed)

    @patch('builtins.input', side_effect=['m'])
    @patch('random.randrange', side_effect=[90, 40])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_boss_battle_lose_output(self, mock_output, mock_random, mock_input):
        with self.assertRaises(SystemExit) as end:
            boss = {'Name': "Jem'Hadar", 'Move': 'stabs', 'HP': 150, 'Attack': 100, 'EXP Earned': 65,
                    'Weapon': "Kar'takin"}
            character = {'Name': 'Testy McTesterson', 'Division': 'Medical', 'HP': 100, 'Melee Attack': 150,
                         'Long-Range Attack': 35, 'Level': 1, 'EXP': 0, 'X-Coordinate': 0, 'Y-Coordinate': 0,
                         'Max HP': 100, 'Title': 'Ensign',
                         'Melee Weapon': 'KaBar Combat Knife', 'Long-Range Weapon': 'type 1 phaser'}
            boss_battle(character, boss)
            expected_output = f"\nI'm sorry, {character['Title']} {character['Name']}" \
                              f"\nYou died.. all though I don't know how you managed that..." \
                              f"\nWe will miss you and give you a proper space funeral."
            game_printed = mock_output.getvalue()
            self.assertIn(expected_output, game_printed)

    @patch('builtins.input', side_effect=['m', 'm', 'm', 'm', 'm'])
    @patch('random.randrange', side_effect=[70, 70, 70, 70, 70])
    def test_boss_battle_boss_dictionary_changed(self,  mock_random, mock_input):
        with self.assertRaises(SystemExit) as end:
            boss = {'Name': "Jem'Hadar", 'Move': 'stabs', 'HP': 150, 'Attack': 30, 'EXP Earned': 65,
                    'Weapon': "Kar'takin"}
            character = {'Name': 'Testy McTesterson',  'HP': 100, 'Melee Attack': 50,
                         'Long-Range Attack': 35, 'Level': 1, 'EXP': 0, 'X-Coordinate': 0, 'Y-Coordinate': 0,
                         'Max HP': 100, 'Division': 'Medical', 'Title': 'Ensign',
                         'Melee Weapon': 'KaBar Combat Knife', 'Long-Range Weapon': 'type 1 phaser'}
            expected = {'Name': "Jem'Hadar", 'Move': 'stabs', 'HP': 0, 'Attack': 60, 'EXP Earned': 65,
                        'Weapon': "Kar'takin"}
            self.assertEqual(expected, boss_battle(character, boss))

    @patch('builtins.input', side_effect=['m', 'm', 'm', 'm', 'm'])
    @patch('random.randrange', side_effect=[90, 40, 90, 40])
    def test_boss_battle_character_dictionary_changed(self,  mock_random, mock_input):
        with self.assertRaises(SystemExit) as end:
            boss = {'Name': "Jem'Hadar", 'Move': 'stabs', 'HP': 150, 'Attack': 50, 'EXP Earned': 65,
                    'Weapon': "Kar'takin"}
            character = {'Name': 'Testy McTesterson',  'HP': 100, 'Melee Attack': 50,
                         'Long-Range Attack': 35, 'Level': 1, 'EXP': 0, 'X-Coordinate': 0, 'Y-Coordinate': 0,
                         'Max HP': 100, 'Division': 'Medical', 'Title': 'Ensign',
                         'Melee Weapon': 'KaBar Combat Knife', 'Long-Range Weapon': 'type 1 phaser'}
            expected = {'Name': 'Testy McTesterson',  'HP': 0, 'Melee Attack': 50,
                        'Long-Range Attack': 35, 'Level': 1, 'EXP': 0, 'X-Coordinate': 0, 'Y-Coordinate': 0,
                        'Max HP': 100, 'Division': 'Medical', 'Title': 'Ensign',
                        'Melee Weapon': 'KaBar Combat Knife', 'Long-Range Weapon': 'type 1 phaser'}
            self.assertEqual(expected, boss_battle(character, boss))
