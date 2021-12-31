from unittest import TestCase
from game import make_board as make_board
from unittest.mock import patch


class TestMakeBoard(TestCase):
    @patch('random.randint', side_effect=[0, 5, 7, 4])
    def test_make_board(self, mock_random):
        rows = 2
        columns = 2
        expected = {(0, 0): 'The Bridge', (0, 1): 'Auxiliary Control', (1, 0): 'Sick Bay', (1, 1): 'Transporter Room'}
        actual = make_board(rows, columns)
        self.assertEqual(actual, expected)
