import unittest
from minesweeper import Minesweeper

CELL_SIZE = 31


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

    def test_reveal_mine_causes_game_over(self):
        self.board.mines.add((2, 2))
        result = self.board.reveal(2, 2)
        self.assertEqual(result, False)
        game_over = self.board.game_over
        self.assertEqual(game_over, True)
    
    def test_add_flag(self):
        self.board.add_flag(1,1)
        self.assertEqual(self.board.flagged, {(1,1)})
    
    def test_add_flag_removes_already_flagged(self):
        self.board.add_flag(1,1)
        self.board.add_flag(2,1)
        self.board.add_flag(1,1)
        self.assertEqual(self.board.flagged, {(2,1)})
    
    def test_remove_flag(self):
        self.board.flagged.add((1,1))
        self.board.flagged.add((2,1))
        self.board.remove_flag(1,1)
        self.assertEqual(self.board.flagged, {(2,1)})
    
    def test_add_move(self):
        self.board.add_move()
        self.assertEqual(self.board.get_moves(), 1)

    def test_is_won_returns_True(self):
        board3 = Minesweeper(3,3,2, CELL_SIZE)
        board3.revealed = {(0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0)}
        self.assertEqual(board3.is_won(), True)
    
    def test_is_won_returns_False(self):
        board4 = Minesweeper(3,3,2, CELL_SIZE)
        board4.revealed = {(0,0), (0,1), (0,2), (1,0), (1,1)}
        self.assertEqual(board4.is_won(), False)

    def test_is_lost_returns_True(self):
        board5 = Minesweeper(3,3,2, CELL_SIZE)
        board5.game_over = True
        self.assertEqual(board5.is_lost(), True)
    
    def test_is_lost_returns_False(self):
        board6 = Minesweeper(3,3,2, CELL_SIZE)
        self.assertEqual(board6.is_lost(), False)