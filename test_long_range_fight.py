from unittest import TestCase
from unittest.mock import patch
from game import long_range_fight as long_range_fight
import io


class TestLongRangeFight(TestCase):
    @patch('random.randrange', return_value=70)
    def test_long_range_fight_hit_success(self, mock_random):
        character = {'Name': 'Testy McTesterson', 'Division': 'Medical', 'Melee Attack': 30, 'HP': 100,
                     'Long-Range Attack': 35, 'Title': 'Ensign', 'Long-Range Weapon': 'type 1 phaser'}
        enemy = {'Name': "Jem'Hadar", 'HP': 150, 'Attack': 40, 'EXP Earned': 65, 'Weapon': "Kar'takin",
                 'Move': 'stabs'}
        expected = {'Name': "Jem'Hadar", 'HP': 115, 'Attack': 40, 'EXP Earned': 65, 'Weapon': "Kar'takin",
                    'Move': 'stabs'}
        actual = long_range_fight(character, enemy)
        self.assertEqual(actual, expected)

    @patch('random.randrange', return_value=70)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_long_range_fight_hit_success_output(self, mock_output, mock_random):
        enemy = {'Name': "Jem'Hadar", 'HP': 150, 'Attack': 40, 'EXP Earned': 65, 'Weapon': "Kar'takin",
                 'Move': 'stabs'}
        character = {'Name': 'Testy McTesterson', 'Division': 'Medical', 'HP': 100, 'Melee Attack': 30,
                     'Long-Range Attack': 35, 'Title': 'Ensign', 'Long-Range Weapon': 'type 1 phaser'}
        long_range_fight(character, enemy)
        expected_output = f"\nWOW! Your {character['Long-Range Weapon']} just blasted the enemy for " \
                          f"{character['Long-Range Attack']} damage!"
        game_printed = mock_output.getvalue()
        self.assertIn(expected_output, game_printed)

    @patch('random.randrange', side_effect=[90, 50])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_long_range_fight_miss_without_damage(self, mock_output, mock_random):
        character = {'Name': 'Testy McTesterson', 'Division': 'Medical', 'HP': 100, 'Melee Attack': 30,
                     'Long-Range Attack': 35, 'Title': 'Ensign', 'Long-Range Weapon': 'type 1 phaser'}
        enemy = {'Name': "Jem'Hadar", 'HP': 150, 'Attack': 40, 'EXP Earned': 65, 'Weapon': "Kar'takin",
                 'Move': 'stabs'}
        long_range_fight(character, enemy)
        expected_output = f"Eek! You just made a nice mark in the wall, {character['Title']} {character['Name']}!"
        game_printed = mock_output.getvalue()
        self.assertIn(expected_output, game_printed)

    @patch('random.randrange', side_effect=[90, 49])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_long_range_fight_miss_with_damage(self, mock_output, mock_random):
        character = {'Name': 'Testy McTesterson', 'Division': 'Medical', 'HP': 100, 'Melee Attack': 30,
                     'Long-Range Attack': 35, 'Long-Range Weapon': 'type 1 phaser', 'Title': 'Ensign', }
        enemy = {'Name': "Jem'Hadar", 'HP': 150, 'Attack': 40, 'EXP Earned': 65, 'Weapon': "Kar'takin",
                 'Move': 'stabs'}
        expected = {'Name': 'Testy McTesterson', 'Division': 'Medical', 'HP': 60, 'Melee Attack': 30,
                    'Long-Range Attack': 35, 'Long-Range Weapon': 'type 1 phaser', 'Title': 'Ensign'}
        actual = long_range_fight(character, enemy)
        self.assertEqual(actual, expected)

    @patch('random.randrange', side_effect=[90, 49])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_long_range_fight_miss_with_damage_output(self, mock_output, mock_random):
        enemy = {'Name': "Jem'Hadar", 'Move': 'stabs', 'HP': 150, 'Attack': 40, 'EXP Earned': 65, 'Weapon': "Kar'takin"}
        character = {'Name': 'Testy McTesterson', 'Division': 'Medical', 'HP': 100, 'Melee Attack': 30,
                     'Long-Range Weapon': 'type 1 phaser', 'Long-Range Attack': 35, 'Title': 'Ensign'}
        long_range_fight(character, enemy)
        expected_output = f"\nYou're going to feel that {enemy['Weapon']} hit for {enemy['Attack']} " \
                          f"damage in the morning."
        game_printed = mock_output.getvalue()
        self.assertIn(expected_output, game_printed)
