import random
import pygame
from sprites.mine import Mine
from sprites.empty import Empty
from sprites.number import Number
from sprites.unopened import Unopened

class Board:
    def __init__(self, cols, rows, mines, cell_size) -> None:
        self.cell_size = cell_size
        self.cols = cols
        self.rows = rows
        self.num_mines = mines
        
        self.mines = pygame.sprite.Group()
        self.empty = pygame.sprite.Group()
        self.numbers = pygame.sprite.Group()
        self.unopened = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        self.mine_coordinates = []

        self.set_board()
        self._initialize_sprites()

    def set_board(self):
        self.board = [["-" for i in range(self.cols)] for j in range(self.rows)]
        for k in range(self.num_mines):
            col = random.randint(0, self.cols-1)
            row = random.randint(0, self.rows-1)
            self.board[row][col] = "X"
            self.mine_coordinates.append((col, row))
    
    def get_board(self):
        return self.board

    def get_num_mines(self):
        return self.num_mines

    def _initialize_sprites(self):
        height = len(self.board)
        width = len(self.board[0])

        for y in range(height):
            for x in range(width):
                cell = self.board[y][x]
                norm_x = x * self.cell_size
                norm_y = y * self.cell_size

                if cell == "X":
                    self.mines.add(Mine(norm_x, norm_y))
                elif cell == "-":
                    self.unopened.add(Unopened(norm_x, norm_y))
                elif cell == 0:
                    self.empty.add(Empty(norm_x, norm_y))
                else:
                    self.numbers.add(Number(norm_x, norm_y, cell))          

        self.all_sprites.add(
            self.mines,
            self.empty,
            self.numbers,
            self.unopened
        )