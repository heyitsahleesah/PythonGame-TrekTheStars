from unittest import TestCase
from game import level_up as level_up


class TestLevelUp(TestCase):
    def test_level_up_level_two(self):
        character = {'Name': 'Testy McTesterson', 'Division': 'Medical', 'HP': 100, 'Melee Attack': 30,
                     'Long-Range Attack': 35, 'Level': 2, 'EXP': 200, 'Max HP': 0, 'Title': 'Ensign'}
        actual = level_up(character)
        expected = {'Name': 'Testy McTesterson', 'Division': 'Medical', 'HP': 150,
                    'Melee Attack': 40, 'Long-Range Attack': 45, 'Level': 2, 'EXP': 200, 'Max HP': 150,
                    'Title': 'Lieutenant Junior Grade'}
        self.assertTrue(actual, expected)

    def test_level_up_level_three(self):
        character = {'Name': 'Testy McTesterson', 'Division': 'Medical', 'HP': 150, 'Melee Attack': 40,
                     'Long-Range Attack': 45, 'Level': 3, 'EXP': 455, 'Title': 'Lieutenant Junior Grade'}
        actual = level_up(character)
        expected = {'Name': 'Testy McTesterson', 'Division': 'Medical', 'HP': 300,
                    'Melee Attack': 50, 'Long-Range Attack': 55, 'Level': 3, 'EXP': 455, 'Max HP': 300,
                    'Title': 'Lieutenant'}
        self.assertTrue(actual, expected)
