from unittest import TestCase
from game import hp_regeneration as hp_regeneration


class TestHpRegeneration(TestCase):
    def test_hp_regeneration_full_health_engineering(self):
        character = {'Division': 'Engineering', 'X-Coordinate': 1, 'Y-Coordinate': 1, 'HP': 10, 'Max HP': 10}
        expected = {'Division': 'Engineering', 'X-Coordinate': 1, 'Y-Coordinate': 1, 'HP': 10, 'Max HP': 10}
        actual = hp_regeneration(character)
        self.assertEqual(actual, expected)

    def test_hp_regeneration_full_health_medical(self):
        character = {'Division': 'Medical', 'X-Coordinate': 1, 'Y-Coordinate': 1, 'HP': 10, 'Max HP': 10}
        expected = {'Division': 'Medical', 'X-Coordinate': 1, 'Y-Coordinate': 1, 'HP': 10, 'Max HP': 10}
        actual = hp_regeneration(character)
        self.assertEqual(actual, expected)

    def test_hp_regeneration_full_health_command(self):
        character = {'Division': 'Command', 'X-Coordinate': 1, 'Y-Coordinate': 1, 'HP': 10, 'Max HP': 10}
        expected = {'Division': 'Command', 'X-Coordinate': 1, 'Y-Coordinate': 1, 'HP': 10, 'Max HP': 10}
        actual = hp_regeneration(character)
        self.assertEqual(actual, expected)

    def test_hp_regeneration_full_health_security(self):
        character = {'Division': 'Security', 'X-Coordinate': 1, 'Y-Coordinate': 1, 'HP': 10, 'Max HP': 10}
        expected = {'Division': 'Security', 'X-Coordinate': 1, 'Y-Coordinate': 1, 'HP': 10, 'Max HP': 10}
        actual = hp_regeneration(character)
        self.assertEqual(actual, expected)

    def test_hp_regeneration_medical(self):
        character = {'Division': 'Medical', 'X-Coordinate': 1, 'Y-Coordinate': 1, 'HP': 5, 'Max HP': 10}
        expected = {'Division': 'Medical', 'X-Coordinate': 1, 'Y-Coordinate': 1, 'HP': 10, 'Max HP': 10}
        actual = hp_regeneration(character)
        self.assertEqual(actual, expected)

    def test_hp_regeneration_engineering(self):
        character = {'Division': 'Engineering', 'X-Coordinate': 1, 'Y-Coordinate': 1, 'HP': 5, 'Max HP': 10}
        expected = {'Division': 'Engineering', 'X-Coordinate': 1, 'Y-Coordinate': 1, 'HP': 7, 'Max HP': 10}
        actual = hp_regeneration(character)
        self.assertEqual(actual, expected)

    def test_hp_regeneration_command(self):
        character = {'Division': 'Command', 'X-Coordinate': 1, 'Y-Coordinate': 1, 'HP': 5, 'Max HP': 10}
        expected = {'Division': 'Command', 'X-Coordinate': 1, 'Y-Coordinate': 1, 'HP': 7, 'Max HP': 10}
        actual = hp_regeneration(character)
        self.assertEqual(actual, expected)

    def test_hp_regeneration_security(self):
        character = {'Division': 'Security', 'X-Coordinate': 1, 'Y-Coordinate': 1, 'HP': 5, 'Max HP': 10}
        expected = {'Division': 'Security', 'X-Coordinate': 1, 'Y-Coordinate': 1, 'HP': 7, 'Max HP': 10}
        actual = hp_regeneration(character)
        self.assertEqual(actual, expected)
