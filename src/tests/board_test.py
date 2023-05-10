import unittest
from game.board import Board

CELL_SIZE = 31


class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board(8, 9, 6)

    def test_board_exists(self):
        self.assertNotEqual(self.board, None)

    def test_board_dimensions(self):
        height = self.board.height
        width = self.board.width
        self.assertEqual(height, 9)
        self.assertEqual(width, 8)

    def test_set_num_mines(self):
        mines = self.board.num_mines
        self.assertEqual(mines, 6)

    def test_reveal_x_y_negative_returns_False(self):
        board = Board(5, 5, 2)
        result = board.reveal(-1, -1)
        self.assertEqual(result, False)

    def test_reveal_x_negative_returns_False(self):
        board = Board(5, 5, 2)
        result = board.reveal(-1, 4)
        self.assertEqual(result, False)

    def test_reveal_y_negative_returns_False(self):
        board = Board(5, 5, 2)
        result = board.reveal(4, -4)
        self.assertEqual(result, False)

    def test_reveal_x_y_board_overflow_returns_False(self):
        board = Board(5, 5, 2)
        result = board.reveal(10, 10)
        self.assertEqual(result, False)

    def test_reveal_x_board_overflow_returns_False(self):
        board = Board(5, 5, 2)
        result = board.reveal(6, 3)
        self.assertEqual(result, False)

    def test_reveal_y_board_overflow_returns_False(self):
        board = Board(5, 5, 2)
        result = board.reveal(4, 7)
        self.assertEqual(result, False)

    def test_reveal_mine_causes_game_over(self):
        board = Board(10, 10, 2)
        board.mines.add((2, 2))
        result = board.reveal(2, 2)
        self.assertEqual(result, False)
        game_over = board.game_over
        self.assertEqual(game_over, True)

    def test_reveal_all_tiles_opened_game_over(self):
        board = Board(2, 2, 0)
        board.reveal(0, 0)
        board.reveal(0, 1)
        board.reveal(1, 0)
        board.reveal(1, 1)
        self.assertEqual(board.game_over, True)

    def test_reveal_continues(self):
        board = Board(10, 10, 0)
        board.mines.add((2, 2))
        result = board.reveal(1, 1)
        self.assertEqual(result, True)
        game_over = board.game_over
        self.assertEqual(game_over, False)

    def test_reveal_count_clicks(self):
        board = Board(10, 10, 0)
        board.mines.add((2, 1))
        board.reveal(1, 1)
        self.assertEqual(board.moves, 1)

        result = board.reveal(3, 1, click=1)
        self.assertEqual(board.moves, 2)
        self.assertEqual(result, True)

        result = board.reveal(0, 1, click=0)
        self.assertEqual(board.moves, 2)
        self.assertEqual(result, True)

    def test_reveal_already_revealed(self):
        board = Board(10, 10, 0)
        board.mines.add((2, 1))
        board.reveal(1, 1)
        result = board.reveal(1, 1)
        board.reveal(0, 1)
        self.assertEqual(result, True)

    def test_add_flag(self):
        board = Board(10, 10, 5)
        board.add_flag(1, 1)
        self.assertEqual(board.flagged, {(1, 1)})

    def test_add_flag_revealed_tile(self):
        board = Board(10, 10, 5)
        board.revealed.add((1, 1))
        board.add_flag(1, 1)
        self.assertEqual(board.flagged, set())

    def test_add_flag_removes_already_flagged(self):
        board = Board(10, 10, 5)
        board.add_flag(1, 1)
        board.add_flag(2, 1)
        board.add_flag(1, 1)
        self.assertEqual(board.flagged, {(2, 1)})

    def test_remove_flag(self):
        board = Board(10, 10, 5)
        board.flagged.add((1, 1))
        board.flagged.add((2, 1))
        board.remove_flag(1, 1)
        self.assertEqual(board.flagged, {(2, 1)})

    def test_num_adjecent_mines(self):
        board = Board(5, 5, 0)
        board.mines.add((1, 1))
        num = board.get_num_adjacent_mines(0, 1)
        self.assertEqual(num, 1)
