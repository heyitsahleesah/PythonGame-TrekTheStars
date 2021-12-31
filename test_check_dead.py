from unittest import TestCase
from game import check_dead as check_dead


class TestCheckDead(TestCase):
    def test_check_dead(self):
        character = {'Name': 'Testy McTesterson', 'Division': 'Medical', 'HP': 0, 'Melee Attack': 30,
                     'Long-Range Attack': 35, 'Level': 1, 'EXP': 0, 'X-Coordinate': 0, 'Y-Coordinate': 0}
        expected = True
        actual = check_dead(character)
        self.assertEqual(actual, expected)

    def test_check_not_dead(self):
        character = {'Name': 'Testy McTesterson', 'Division': 'Medical', 'HP': 100, 'Melee Attack': 30,
                     'Long-Range Attack': 35, 'Level': 1, 'EXP': 0, 'X-Coordinate': 0, 'Y-Coordinate': 0}
        expected = False
        actual = check_dead(character)
        self.assertEqual(actual, expected)

    def test_check_dead_character_not_changed(self):
        character = {'Name': 'Testy McTesterson', 'Division': 'Medical', 'HP': 100, 'Melee Attack': 30,
                     'Long-Range Attack': 35, 'Level': 1, 'EXP': 0, 'X-Coordinate': 0, 'Y-Coordinate': 0}
        check_dead(character)
        self.assertTrue(character, {'Name': 'Testy McTesterson', 'Division': 'Medical', 'HP': 100, 'Melee Attack': 30,
                                    'Long-Range Attack': 35, 'Level': 1, 'EXP': 0, 'X-Coordinate': 0,
                                    'Y-Coordinate': 0})
