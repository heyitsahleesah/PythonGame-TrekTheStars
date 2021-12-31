from unittest import TestCase
from unittest.mock import patch
from game import melee_fight as melee_fight
import io


class TestMeleeFight(TestCase):
    @patch('random.randrange', return_value=70)
    def test_melee_fight_hit_success(self, mock_random):
        character = {'Name': 'Testy McTesterson', 'Division': 'Medical', 'HP': 100, 'Melee Attack': 30,
                     'Long-Range Attack': 35, 'Melee Weapon': 'KaBar Combat Knife', 'Title': 'Ensign'}
        enemy = {'Name': "Jem'Hadar", 'HP': 150, 'Attack': 40, 'EXP Earned': 65, 'Weapon': "Kar'takin",
                 'Move': 'stabs'}
        expected = {'Name': "Jem'Hadar", 'HP': 120, 'Attack': 40, 'EXP Earned': 65, 'Weapon': "Kar'takin",
                    'Move': 'stabs'}
        actual = melee_fight(character, enemy)
        self.assertEqual(actual, expected)

    @patch('random.randrange', return_value=70)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_melee_fight_hit_success_output(self, mock_output, mock_random):
        character = {'Name': 'Testy McTesterson', 'Division': 'Medical', 'HP': 100, 'Melee Attack': 30,
                     'Long-Range Attack': 35, 'Title': 'Ensign', 'Melee Weapon': 'KaBar Combat Knife'}
        enemy = {'Name': "Jem'Hadar", 'HP': 150, 'Attack': 40, 'EXP Earned': 65, 'Weapon': "Kar'takin",
                 'Move': 'stabs'}
        melee_fight(character, enemy)
        expected_output = f"\nNice. You swung your {character['Melee Weapon']} at the {enemy['Name']} and did" \
                          f" {character['Melee Attack']} damage."
        game_printed = mock_output.getvalue()
        self.assertIn(expected_output, game_printed)

    @patch('random.randrange', side_effect=[80, 50])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_melee_fight_miss_without_damage(self, mock_output, mock_random):
        character = {'Name': 'Testy McTesterson', 'Title': 'Ensign', 'Division': 'Medical', 'HP': 100, 'Melee Attack': 30,
                     'Long-Range Attack': 35, }
        enemy = {'Name': "Jem'Hadar", 'HP': 150, 'Attack': 40, 'EXP Earned': 65, 'Weapon': "Kar'takin",
                 'Move': 'stabs'}
        melee_fight(character, enemy)
        expected_output = f"\nOOF. You swung wide and missed!"
        game_printed = mock_output.getvalue()
        self.assertIn(expected_output, game_printed)

    @patch('random.randrange', side_effect=[80, 40])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_melee_fight_miss_with_damage_output(self, mock_output, mock_random):
        enemy = {'Name': "Jem'Hadar", 'HP': 150, 'Attack': 40, 'EXP Earned': 65, 'Weapon': "Kar'takin",
                 'Move': 'stabs'}
        character = {'Name': 'Testy McTesterson', 'Division': 'Medical', 'HP': 100, 'Melee Attack': 30,
                     'Long-Range Attack': 35, 'Title': 'Ensign', 'Melee Weapon': 'KaBar Combat Knife'}
        melee_fight(character, enemy)
        expected_output = f"\nYour opponent {enemy['Move']} at you with their {enemy['Weapon']}! It did a " \
                          f"\nwhopping {enemy['Attack']} damage!"
        game_printed = mock_output.getvalue()
        self.assertIn(expected_output, game_printed)

    @patch('random.randrange', side_effect=[80, 40])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_melee_fight_miss_with_damage(self, mock_output, mock_random):
        enemy = {'Name': "Jem'Hadar", 'HP': 150, 'Attack': 40, 'EXP Earned': 65, 'Weapon': "Kar'takin",
                 'Move': 'stabs'}
        character = {'Name': 'Testy McTesterson', 'Division': 'Medical', 'HP': 100, 'Melee Attack': 30,
                     'Long-Range Attack': 35, 'Title': 'Ensign'}
        expected = {'Name': 'Testy McTesterson', 'Division': 'Medical', 'HP': 60, 'Melee Attack': 30,
                    'Long-Range Attack': 35, 'Title': 'Ensign'}
        actual = melee_fight(character, enemy)
        self.assertEqual(actual, expected)
