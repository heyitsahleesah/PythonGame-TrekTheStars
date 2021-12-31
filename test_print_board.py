from unittest import TestCase
from unittest.mock import patch
from game import print_board as print_board
from game import make_board as make_board
import io


class TestPrintBoard(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_board_boss(self, mock_output):
        rows = 10
        columns = 10
        character = {'X-Coordinate': 2, 'Y-Coordinate': 2}
        board = make_board(rows, columns)
        print_board(board, rows, columns, character)
        game_printed = mock_output.getvalue()
        expected_output = '[!]'
        self.assertIn(expected_output, game_printed)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_board_character(self, mock_output):
        rows = 10
        columns = 10
        character = {'X-Coordinate': 2, 'Y-Coordinate': 2}
        board = make_board(rows, columns)
        print_board(board, rows, columns, character)
        game_printed = mock_output.getvalue()
        expected_output = '[*]'
        self.assertIn(expected_output, game_printed)

    def test_print_board_character_unchanged(self):
        rows = 10
        columns = 10
        character = {'X-Coordinate': 2, 'Y-Coordinate': 2}
        board = make_board(rows, columns)
        print_board(board, rows, columns, character)
        self.assertTrue(character, {'X-Coordinate': 2, 'Y-Coordinate': 2})
