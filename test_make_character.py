from unittest import TestCase
from game import make_character as make_character


class TestMakeCharacter(TestCase):
    def test_make_character(self):
        character = {'Name': 'Testy McTesterson', 'Title': 'Ensign'}
        character_class = {'Division': 'Medical', 'HP': 100, 'Melee Attack': 30, 'Long-Range Attack': 35,
                           'Melee Weapon': 'KaBar Combat Knife', 'Long-Range Weapon': 'type 1 phaser'}
        expected = {'Name': 'Testy McTesterson', 'Division': 'Medical', 'HP': 100, 'Melee Attack': 30,
                    'Long-Range Attack': 35, 'Level': 1, 'EXP': 0, 'X-Coordinate': 0, 'Y-Coordinate': 0, 'Max HP': 100,
                    'Title': 'Ensign',  'Melee Weapon': 'KaBar Combat Knife', 'Long-Range Weapon': 'type 1 phaser'}
        actual = make_character(character, character_class)
        self.assertEqual(actual, expected)

    def test_make_character_class_unchanged(self):
        character = {'Name': 'Testy McTesterson'}
        character_class = {'Division': 'Medical', 'HP': 100, 'Melee Attack': 30, 'Long-Range Attack': 35,
                           'Melee Weapon': 'KaBar Combat Knife', 'Long-Range Weapon': 'type 1 phaser'}
        make_character(character, character_class)
        self.assertTrue(character_class, {'Division': 'Medical', 'HP': 100, 'Melee Attack': 30, 'Long-Range Attack': 35,
                                          'Melee Weapon': 'KaBar Combat Knife', 'Long-Range Weapon': 'type 1 phaser'})
