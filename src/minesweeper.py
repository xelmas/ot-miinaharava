import random
import pygame
from sprites.mine import Mine
from sprites.empty import Empty
from sprites.adjecent import Adjecent
from sprites.unrevealed import Unrevealed

class Minesweeper:

    def __init__(self, width, height, num_mines, cell_size) -> None:
        self.width = width
        self.height = height
        self.num_mines = num_mines
        self.mines = set()
        self.revealed = set()
        self.game_over = False
        self.board = [["" for _ in range(self.width)] for _ in range(self.height)]
        self.cell_size = cell_size
        self.mine_tiles = pygame.sprite.Group()
        self.empty_tiles = pygame.sprite.Group()
        self.adjecent_tiles = pygame.sprite.Group()
        self.unrevealed_tiles = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        self.place_mines()
        self._initialize_sprites()

    def place_mines(self):
        for _ in range(self.num_mines):
            while True:
                x = random.randint(0, self.width- 1)
                y = random.randint(0, self.height - 1)

                if (x, y) not in self.mines:
                    self.mines.add((x, y))
                    self.board[y][x] = "x"
                    break

    def get_neighbors(self, x, y):
        """ 
        list values -1, 0, 1 determine the changes in x and y coordinates so that all possible 8 neighbors are found.
        Returns neighbors coordinates as a list of tuples (x_cor, y_cor).
        """
        result = []
        for x_cor in [-1, 0, 1]:
            for y_cor in [-1, 0, 1]:
                if x_cor == 0 and y_cor == 0:
                    continue
                new_x = x + x_cor
                new_y = y + y_cor
                
                if 0 <= new_x < self.width and 0 <= new_y < self.height:
                    result.append((new_x, new_y))
        print("neighbors for", x,y, "is", result)
        return result
    
    def get_num_adjacent_mines(self, x, y):
        count = 0
        neighbors = self.get_neighbors(x, y)

        for x_cor, y_cor in neighbors:
            if (x_cor, y_cor) in self.mines:
                count += 1
        return count
    
    def reveal(self, x, y):
        if (x, y) in self.mines:
            self.game_over = True
            return False

        if (x, y) not in self.revealed:
            self.revealed.add((x, y))
            
            
        num_all_tiles = self.width * self.height - self.num_mines
        if len(self.revealed) == num_all_tiles:
            self.game_over = True
            return True

        num_adjecent_mines = self.get_num_adjacent_mines(x, y)
        if num_adjecent_mines == 0:
            self.board[y][x] = " "
            for x_cor, y_cor in self.get_neighbors(x, y):
                if (x_cor, y_cor) not in self.revealed:
                    self.reveal(x_cor, y_cor)
        else:
            self.board[y][x] = num_adjecent_mines

        return True
    
    def get_board(self):
        return self.board

    def get_num_mines(self):
        return self.num_mines
    
    def print_board(self):
        for i in range(len(self.board)):
            print(self.board[i])
        print()             
    
    def play(self):
        while not self.game_over:
            self.print_board()
            
            x = int(input("Enter x coordinate: "))
            y = int(input("Enter y coordinate: "))
            self.reveal(x, y)

        num_all_tiles = self.width * self.height - self.num_mines
        if self.game_over and len(self.revealed) == num_all_tiles:
            print("You won!")
        else:
            print("Game over")
    
    def _initialize_sprites(self):
        height = len(self.board)
        width = len(self.board[0])

        for y in range(height):
            for x in range(width):
                cell = self.board[y][x]
                norm_x = x * self.cell_size
                norm_y = y * self.cell_size

                if cell == "x":
                    self.mine_tiles.add(Mine(norm_x, norm_y))
                elif cell == "":
                    self.unrevealed_tiles.add(Unrevealed(norm_x, norm_y))
                elif cell == " ":
                    self.empty_tiles.add(Empty(norm_x, norm_y))
                else:
                    self.adjecent_tiles.add(Adjecent(norm_x, norm_y, cell))          

        self.all_sprites.add(
            self.mine_tiles,
            self.empty_tiles,
            self.adjecent_tiles,
            self.unrevealed_tiles
        )
    
