import unittest
from minesweeper import Minesweeper

CELL_SIZE = 50


class TestMinesweeper(unittest.TestCase):
    def setUp(self):
        self.board = Minesweeper(8, 9, 6, CELL_SIZE)

    def test_board_exists(self):
        self.assertNotEqual(self.board, None)

    def assert_coordinates_equal(self, sprite, x, y):
        self.assertEqual(sprite.rect.x, x)
        self.assertEqual(sprite.rect.y, y)

    def test_board_dimensions(self):
        height = len(self.board.get_board())
        width = len(self.board.get_board()[0])
        self.assertEqual(height, 9)
        self.assertEqual(width, 8)

    def test_set_num_mines(self):
        mines = self.board.get_num_mines()
        self.assertEqual(mines, 6)

    def test_reveal_x_y_negative_returns_False(self):
        result = self.board.reveal(-1, -1)
        self.assertEqual(result, False)

    def test_reveal_x_negative_returns_False(self):
        result = self.board.reveal(-1, 4)
        self.assertEqual(result, False)

    def test_reveal_y_negative_returns_False(self):
        result = self.board.reveal(4, -4)
        self.assertEqual(result, False)

    def test_reveal_x_y_board_overflow_returns_False(self):
        result = self.board.reveal(10, 10)
        self.assertEqual(result, False)

    def test_reveal_x_board_overflow_returns_False(self):
        result = self.board.reveal(10, 9)
        self.assertEqual(result, False)

    def test_reveal_y_board_overflow_returns_False(self):
        result = self.board.reveal(8, 11)
        self.assertEqual(result, False)

    def test_reveal_x_y_positive_returns_True(self):
        result = self.board.reveal(1, 1)
        self.assertEqual(result, True)

    def test_reveal_x_y_zero_returns_True(self):
        result = self.board.reveal(0, 0)
        self.assertEqual(result, True)

    def test_reveal_mine_causes_game_over(self):
        self.board.mines.add((2, 2))
        result = self.board.reveal(2, 2)
        self.assertEqual(result, False)
        game_over = self.board.game_over
        self.assertEqual(game_over, True)
