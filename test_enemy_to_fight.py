from unittest import TestCase
from unittest.mock import patch
from game import enemy_to_fight as enemy_to_fight


class TestEnemyToFight(TestCase):
    @patch('random.randint', return_value=6)
    def test_enemy_to_fight(self, mock_random):
        expected = {'Name': "Jem'Hadar", 'HP': 150, 'Attack': 40, 'EXP Earned': 80, 'Weapon': "Kar'takin",
                    'Move': 'stabs'}
        actual = enemy_to_fight()
        self.assertEqual(actual, expected)

