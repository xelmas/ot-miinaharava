import unittest
from pygame.sprite import AbstractGroup
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

    def test_add_move(self):
        self.game.add_move()
        self.assertEqual(self.game.get_moves(), 1)

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
        game = Minesweeper(3, 3, 2, CELL_SIZE)
        game.board.game_over = True
        self.assertEqual(game.is_lost(), True)

    def test_is_lost_returns_False(self):
        game = Minesweeper(3, 3, 2, CELL_SIZE)
        self.assertEqual(game.is_lost(), False)

    def test_set_time_passed(self):
        self.game.set_time_passed(8)
        self.assertEqual(self.game.get_time_passed(), 8)

    def test_get_time_passed(self):
        self.game.set_time_passed(9)
        self.assertEqual(self.game.get_time_passed(), 9)
