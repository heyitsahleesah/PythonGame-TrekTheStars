from unittest import TestCase
from game import check_experience as check_experience


class TestCheckExperience(TestCase):
    def test_check_experience_zero(self):
        character = {'Name': 'Testy McTesterson', 'Division': 'Medical', 'HP': 100, 'Melee Attack': 30,
                     'Long-Range Attack': 35, 'Level': 1, 'EXP': 0, 'Max HP': 100, 'Title': 'Ensign'}
        expected = {'Name': 'Testy McTesterson', 'Division': 'Medical', 'HP': 100, 'Melee Attack': 30,
                    'Long-Range Attack': 35, 'Level': 1, 'EXP': 0, 'Max HP': 100, 'Title': 'Ensign'}
        actual = check_experience(character)
        self.assertEqual(actual, expected)

    def test_check_experience_not_levelled(self):
        character = {'Name': 'Testy McTesterson', 'Division': 'Medical', 'HP': 100, 'Melee Attack': 30,
                     'Long-Range Attack': 35, 'Level': 1, 'EXP': 50, 'Max HP': 100, 'Title': 'Ensign'}
        expected = {'Name': 'Testy McTesterson', 'Division': 'Medical', 'HP': 100, 'Melee Attack': 30,
                    'Long-Range Attack': 35, 'Level': 1, 'EXP': 50, 'Max HP': 100, 'Title': 'Ensign'}
        actual = check_experience(character)
        self.assertEqual(actual, expected)

    def test_check_experience_level_two(self):
        character = {'Name': 'Testy McTesterson', 'Division': 'Medical', 'HP': 100, 'Melee Attack': 30,
                     'Long-Range Attack': 35, 'Level': 1, 'EXP': 200, 'Max HP': 0, 'Title': 'Ensign'}
        expected = {'Name': 'Testy McTesterson', 'Division': 'Medical', 'HP': 150,
                    'Melee Attack': 40, 'Long-Range Attack': 45, 'Level': 2, 'EXP': 200, 'Max HP': 150,
                    'Title': 'Lieutenant Junior Grade'}
        actual = check_experience(character)
        self.assertEqual(actual, expected)

    def test_check_experience_level_three_slightly_above_experience(self):
        character = {'Name': 'Testy McTesterson', 'Division': 'Medical', 'HP': 150, 'Melee Attack': 40,
                     'Long-Range Attack': 45, 'Level': 2, 'EXP': 455, 'Title': 'Lieutenant Junior Grade'}
        expected = {'Name': 'Testy McTesterson', 'Division': 'Medical', 'HP': 300,
                    'Melee Attack': 50, 'Long-Range Attack': 55, 'Level': 3, 'EXP': 455, 'Max HP': 300,
                    'Title': 'Lieutenant'}
        actual = check_experience(character)
        self.assertEqual(actual, expected)
