from unittest import TestCase
from game import is_boss as is_boss


class TestIsBoss(TestCase):
    def test_is_boss_false(self):
        rows = 5
        columns = 5
        character = {'Name': 'Testy McTesterson', 'Division': 'Medical', 'HP': 100, 'Melee Attack': 30,
                     'Long-Range Attack': 35, 'Level': 1, 'EXP': 0, 'X-Coordinate': 0, 'Y-Coordinate': 0}
        expected = False
        actual = is_boss(character, rows, columns)
        self.assertEqual(actual, expected)

    def test_is_boss_character_unchanged(self):
        rows = 5
        columns = 5
        character = {'Name': 'Testy McTesterson', 'Division': 'Medical', 'HP': 100, 'Melee Attack': 30,
                     'Long-Range Attack': 35, 'Level': 1, 'EXP': 0, 'X-Coordinate': 0, 'Y-Coordinate': 0}
        is_boss(character, rows, columns)
        self.assertTrue(character, {'Name': 'Testy McTesterson', 'Division': 'Medical', 'HP': 100, 'Melee Attack': 30,
                                    'Long-Range Attack': 35, 'Level': 1, 'EXP': 0, 'X-Coordinate': 0, 'Y-Coordinate': 0})