import unittest
from minesweeper import Minesweeper

CELL_SIZE = 50

class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Minesweeper(8,9,6, CELL_SIZE)
    
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

    