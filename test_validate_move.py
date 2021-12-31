from unittest import TestCase
from game import validate_move as validate_move


class TestValidateMove(TestCase):
    def test_validate_move_false(self):
        board = {(0, 0): "Empty Room", (0, 1): "Empty Room", (1, 0): "Empty Room", (1, 1): "Empty Room"}
        character = {"X-Coordinate": 0, "Y-Coordinate": 0, "HP": 5}
        direction = '1'
        expected = False
        actual = validate_move(board, character, direction)
        self.assertEqual(actual, expected)

    def test_validate_move_true(self):
        board = {(0, 0): "Empty Room", (0, 1): "Empty Room", (1, 0): "Empty Room", (1, 1): "Empty Room"}
        character = {"X-Coordinate": 0, "Y-Coordinate": 0, "HP": 5}
        direction = '2'
        expected = True
        actual = validate_move(board, character, direction)
        self.assertEqual(actual, expected)

    def test_validate_move_board_character_unchanged(self):
        board = {(0, 0): "Empty Room", (0, 1): "Empty Room", (1, 0): "Empty Room", (1, 1): "Empty Room"}
        character = {"X-Coordinate": 0, "Y-Coordinate": 0, "HP": 5}
        direction = '3'
        validate_move(board, character, direction)
        self.assertTrue(board, {(0, 0): "Empty Room", (0, 1): "Empty Room", (1, 0): "Empty Room", (1, 1): "Empty Room"})
        self.assertTrue(character, {"X-Coordinate": 0, "Y-Coordinate": 0, "HP": 5})
