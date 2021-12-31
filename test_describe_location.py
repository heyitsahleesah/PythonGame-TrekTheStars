from unittest import TestCase
from unittest.mock import patch
from game import describe_current_location as describe_current_location
from game import make_board as make_board


class TestDescribeLocation(TestCase):
    @patch('random.randint', side_effect=[0, 1, 2, 3])
    def test_describe_current_location(self, mock_random):
        rows = 2
        columns = 2
        board = make_board(rows, columns)
        character = {"X-Coordinate": 0, "Y-Coordinate": 0, "HP": 5}
        expected = "The Bridge"
        actual = describe_current_location(board, character)
        self.assertEqual(actual, expected)

    @patch('random.randint', side_effect=[0, 1, 2, 3])
    def test_describe_current_location_character_board_dictionary_unchanged(self, mock_random):
        rows = 2
        columns = 2
        board = make_board(rows, columns)
        character = {"X-Coordinate": 0, "Y-Coordinate": 0, "HP": 5}
        describe_current_location(board, character)
        self.assertTrue(board, {(0, 0): 'The Bridge', (0, 1): 'Round Corridor', (1, 0): 'Straight Corridor',
                                (1, 1): 'Main Engineering'})
        self.assertTrue(character, {"X-Coordinate": 0, "Y-Coordinate": 0, "HP": 5})

