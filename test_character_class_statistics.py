from unittest import TestCase
from game import character_class_statistics as character_class_statistics


class TestCharacterClassStatistics(TestCase):
    def test_character_class_statistics(self):
        expected = {'4': {'Division': 'Security', 'HP': 100, 'Melee Attack': 50, 'Long-Range Attack': 25,
                          'Melee Weapon': 'Katana', 'Long-Range Weapon': 'fists'},
                    '1': {'Division': 'Medical', 'HP': 100, 'Melee Attack': 30, 'Long-Range Attack': 35,
                          'Melee Weapon': 'KaBar Combat Knife', 'Long-Range Weapon': 'type 1 phaser'},
                    '2': {'Division': 'Engineering', 'HP': 75, 'Melee Attack': 30, 'Long-Range Attack': 35,
                          'Melee Weapon': 'KaBar Combat Knife', 'Long-Range Weapon': 'type 3 phaser rifle'},
                    '3': {'Division': 'Command', 'HP': 75, 'Melee Attack': 40, 'Long-Range Attack': 35,
                          'Melee Weapon': 'KaBar Combat Knife', 'Long-Range Weapon': 'type 2 phaser pistol'},
                    }
        actual = character_class_statistics()
        self.assertEqual(expected, actual)
