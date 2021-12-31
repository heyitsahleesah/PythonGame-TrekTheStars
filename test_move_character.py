from unittest import TestCase
from game import move_character as move_character


class TestMoveCharacter(TestCase):
    def test_move_character_x_coordinate_negative(self):
        direction = '1'
        character = {"X-Coordinate": 1, "Y-Coordinate": 1, "HP": 3}
        expected = {"X-Coordinate": 0, "Y-Coordinate": 1, "HP": 3}
        actual = move_character(character, direction)
        self.assertEqual(actual, expected)

    def test_move_character_x_coordinate_positive(self):
        direction = '3'
        character = {"X-Coordinate": 0, "Y-Coordinate": 0, "HP": 3}
        expected = {"X-Coordinate": 1, "Y-Coordinate": 0, "HP": 3}
        actual = move_character(character, direction)
        self.assertEqual(actual, expected)

    def test_move_character_y_coordinate_positive(self):
        direction = '2'
        character = {"X-Coordinate": 1, "Y-Coordinate": 1, "HP": 3}
        expected = {"X-Coordinate": 1, "Y-Coordinate": 2, "HP": 3}
        actual = move_character(character, direction)
        self.assertEqual(actual, expected)

    def test_move_character_y_coordinate_negative(self):
        direction = '4'
        character = {"X-Coordinate": 0, "Y-Coordinate": 3, "HP": 3}
        expected = {"X-Coordinate": 0, "Y-Coordinate": 2, "HP": 3}
        actual = move_character(character, direction)
        self.assertEqual(actual, expected)


