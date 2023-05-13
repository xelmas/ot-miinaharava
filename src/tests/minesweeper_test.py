import unittest
from game.minesweeper import Minesweeper
CELL_SIZE = 31


class TestMinesweeper(unittest.TestCase):
    def setUp(self):
        self.game = Minesweeper(8, 9, 6, CELL_SIZE)

    def test_game_exists(self):
        self.assertNotEqual(self.game, None)

    def assert_coordinates_equal(self, sprite, x, y):
        self.assertEqual(sprite.rect.x, x)
        self.assertEqual(sprite.rect.y, y)

    def test_get_moves(self):
        game = Minesweeper(5, 5, 10, CELL_SIZE)
        game.board.add_move()
        game.board.add_move()
        self.assertEqual(game.get_moves(), 2)

    def test_is_won_returns_True(self):
        game = Minesweeper(3, 3, 2, CELL_SIZE)
        game.board.revealed = {(0, 0), (0, 1), (0, 2), (1, 0),
                               (1, 1), (1, 2), (2, 0)}
        self.assertEqual(game.is_won(), True)

    def test_is_won_returns_False(self):
        game = Minesweeper(3, 3, 2, CELL_SIZE)
        game.board.revealed = {(0, 0), (0, 1), (0, 2), (1, 0), (1, 1)}
        self.assertEqual(game.is_won(), False)

    def test_is_lost_returns_True(self):
        game = Minesweeper(5, 5, 2, CELL_SIZE)
        game.board.game_over = True
        self.assertEqual(game.is_lost(), True)

    def test_is_lost_returns_False(self):
        game = Minesweeper(5, 5, 2, CELL_SIZE)
        self.assertEqual(game.is_lost(), False)

    def test_get_game_mines_flagged_info(self):
        game = Minesweeper(10, 10, 5, CELL_SIZE)
        game.board.add_flag(1, 1)
        game.board.add_flag(1, 2)
        game.board.add_flag(1, 3)
        result = game.get_unflagged_mines()
        self.assertEqual(result, 2)

    def test_get_game_mines_flagged_info_not_negative(self):
        game = Minesweeper(10, 10, 5, CELL_SIZE)
        game.board.add_flag(1, 1)
        game.board.add_flag(1, 2)
        game.board.add_flag(1, 3)
        game.board.add_flag(0, 1)
        game.board.add_flag(0, 2)
        game.board.add_flag(0, 3)
        result = game.get_unflagged_mines()
        self.assertEqual(result, 0)

    def test_initialize_mine_tile_sprite(self):
        game = Minesweeper(3, 3, 0, CELL_SIZE)
        x_cor, y_cor, tile_content = 0, 0, "x"
        game.board.mines.add((0, 0))
        game.board.revealed.add((0, 0))
        game._initialize_tile_sprite(x_cor, y_cor, tile_content)
        self.assertEqual(len(game.mine_tiles), 1)

    def test_initialize_empty_tile_sprite(self):
        game = Minesweeper(3, 3, 0, CELL_SIZE)
        x_cor, y_cor, tile_content = 0, 0, " "
        game.board.revealed.add((0, 0))
        game._initialize_tile_sprite(x_cor, y_cor, tile_content)
        self.assertEqual(len(game.empty_tiles), 1)

    def test_initialize_adjacent_tile_sprite(self):
        game = Minesweeper(3, 3, 0, CELL_SIZE)
        x_cor, y_cor, tile_content = 1, 0, 1
        game.board.mines.add((0, 0))
        game.board.revealed.add((1, 0))
        game._initialize_tile_sprite(x_cor, y_cor, tile_content)
        self.assertEqual(len(game.adjacent_tiles), 1)

    def test_initialize_flag_tile_sprite(self):
        game = Minesweeper(3, 3, 0, CELL_SIZE)
        x_cor, y_cor, tile_content = 0, 0, "f"
        game.board.mines.add((0, 0))
        game.board.add_flag(0, 0)
        game._initialize_tile_sprite(x_cor, y_cor, tile_content)
        self.assertEqual(len(game.flag_tiles), 1)

    def test_initialize_tile_sprite_invalid_tile_content(self):
        game = Minesweeper(3, 3, 0, CELL_SIZE)
        game.board.reveal(0, 0)
        game.board.add_flag(0, 1)
        game._initialize_tile_sprite(1, 1, 10)
        self.assertEqual(len(game.adjacent_tiles), 0)
