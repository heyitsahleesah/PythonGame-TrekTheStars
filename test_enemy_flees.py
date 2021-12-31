from unittest import TestCase
from unittest.mock import patch
from game import enemy_flees as enemy_flees
import io


class TestEnemyFlees(TestCase):
    @patch('random.randrange', side_effect=[15])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_enemy_flees_true_output(self, mock_output, mock_random):
        character = {'Name': 'Testy McTesterson', 'Division': 'Medical', 'HP': 100, 'Melee Attack': 150,
                     'Long-Range Attack': 35, 'Level': 1, 'EXP': 0, 'X-Coordinate': 0, 'Y-Coordinate': 0,
                     'Max HP': 100, 'Title': 'Ensign'}
        enemy = {'Name': "Jem'Hadar", 'HP': 150, 'Attack': 40, 'EXP Earned': 80, 'Weapon': "Kar'takin",
                 'Move': 'stabs'}
        enemy_flees(character, enemy)
        expected_output = f"\nLooks like you really scared them, {character['Title']}. They ran away." \
                          f"\nWe're going to have to find them somewhere on the ship though!"
        game_printed = mock_output.getvalue()
        self.assertIn(expected_output, game_printed)

    @patch('random.randrange', side_effect=[19])
    def test_enemy_flees_true(self, mock_random):
        character = {'Name': 'Testy McTesterson', 'Division': 'Medical', 'HP': 100, 'Melee Attack': 150,
                     'Long-Range Attack': 35, 'Level': 1, 'EXP': 0, 'X-Coordinate': 0, 'Y-Coordinate': 0,
                     'Max HP': 100, 'Title': 'Ensign'}
        enemy = {'Name': "Jem'Hadar", 'Attack': 40, 'EXP Earned': 80, 'Weapon': "Kar'takin", 'HP': 150,
                 'Move': 'stabs'}
        expected = True
        actual = enemy_flees(character, enemy)
        self.assertEqual(expected, actual)

    @patch('random.randrange', side_effect=[20])
    def test_enemy_flees_false(self, mock_random):
        character = {'Name': 'Testy McTesterson', 'Division': 'Medical', 'HP': 100, 'Melee Attack': 150,
                     'Long-Range Attack': 35, 'Level': 1, 'EXP': 0, 'X-Coordinate': 0, 'Y-Coordinate': 0,
                     'Max HP': 100, 'Title': 'Ensign'}
        enemy = {'Name': "Jem'Hadar", 'Attack': 40, 'Weapon': "Kar'takin", 'HP': 150,  'EXP Earned': 80,
                 'Move': 'stabs'}
        expected = False
        actual = enemy_flees(character, enemy)
        self.assertEqual(expected, actual)

    @patch('random.randrange', side_effect=[19])
    def test_enemy_flees_character_dictionary_unchanged(self, mock_random):
        character = {'Name': 'Testy McTesterson', 'Division': 'Medical', 'HP': 100, 'Melee Attack': 150,
                     'Long-Range Attack': 35, 'Level': 1, 'EXP': 0, 'X-Coordinate': 0, 'Y-Coordinate': 0,
                     'Max HP': 100, 'Title': 'Ensign'}
        enemy = {'Name': "Jem'Hadar", 'Attack': 40,  'HP': 150,  'EXP Earned': 80, 'Weapon': "Kar'takin",
                 'Move': 'stabs'}
        enemy_flees(character, enemy)
        self.assertTrue(character, {'Name': 'Testy McTesterson', 'Division': 'Medical', 'HP': 100, 'Melee Attack': 150,
                                    'Long-Range Attack': 35, 'Level': 1, 'EXP': 0, 'X-Coordinate': 0, 'Y-Coordinate': 0,
                                    'Max HP': 100, 'Title': 'Ensign'})
