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

        self.board = [["" for _ in range(self.width)]
                      for _ in range(self.height)]
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
                x_cor = random.randint(0, self.width - 1)
                y_cor = random.randint(0, self.height - 1)

                if (x_cor, y_cor) not in self.mines:
                    self.mines.add((x_cor, y_cor))
                    self.board[y_cor][x_cor] = "x"
                    break

    def get_neighbors(self, x_cor, y_cor):
        """ 
        list values -1, 0, 1 determine the changes in x and y coordinates 
        so that all possible 8 neighbors are found.
        Returns neighbors coordinates as a list of tuples (x_cor, y_cor).
        """
        result = []
        for x_cor2 in [-1, 0, 1]:
            for y_cor2 in [-1, 0, 1]:
                if x_cor2 == 0 and y_cor2 == 0:
                    continue
                new_x = x_cor + x_cor2
                new_y = y_cor + y_cor2

                if 0 <= new_x < self.width and 0 <= new_y < self.height:
                    result.append((new_x, new_y))
        return result

    def get_num_adjacent_mines(self, x_cor, y_cor):
        count = 0
        neighbors = self.get_neighbors(x_cor, y_cor)

        for x_cor2, y_cor2 in neighbors:
            if (x_cor2, y_cor2) in self.mines:
                count += 1
        return count

    def reveal(self, x_cor, y_cor):

        if x_cor < 0 or y_cor < 0:
            print("x and y cannot be negative")
            return False
        if x_cor >= self.width or y_cor >= self.height:
            print("Coordinate overflow")
            return False

        if (x_cor, y_cor) in self.mines:
            self.game_over = True
            return False

        if (x_cor, y_cor) not in self.revealed:
            self.revealed.add((x_cor, y_cor))

        num_all_tiles = self.width * self.height - self.num_mines
        if len(self.revealed) == num_all_tiles:
            self.game_over = True
            return True

        num_adjecent_mines = self.get_num_adjacent_mines(x_cor, y_cor)
        if num_adjecent_mines == 0:
            self.board[y_cor][x_cor] = " "
            for x_cor2, y_cor2 in self.get_neighbors(x_cor, y_cor):
                if (x_cor2, y_cor2) not in self.revealed:
                    self.reveal(x_cor2, y_cor2)
        else:
            self.board[y_cor][x_cor] = num_adjecent_mines

        return True

    def get_board(self):
        return self.board

    def get_num_mines(self):
        return self.num_mines

    def print_board(self):
        print("   ", end="")
        for x_cor in range(self.width):
            print(x_cor, end="")
        print()
            
        for y_cor in range(len(self.board)):
            print(y_cor,"|", end="")
            for x_cor in range(len(self.board[y_cor])):
                if (x_cor, y_cor) in self.revealed:
                    print(self.board[y_cor][x_cor], end="")
                else:
                    print("0", end="")
            print("|", end="")
            print()

    def play(self):

        while not self.game_over:
            self.print_board()
            while True:
                try:
                    x_cor = int(input("Enter x coordinate: "))
                    y_cor = int(input("Enter y coordinate: "))
                    self.reveal(x_cor, y_cor)
                    break
                except ValueError:
                    print("Must be digits")

        num_all_tiles = self.width * self.height - self.num_mines
        if self.game_over and len(self.revealed) == num_all_tiles:
            print("You won!")
        else:
            print("Game over")

    def _initialize_sprites(self):
        height = len(self.board)
        width = len(self.board[0])

        for y_cor in range(height):
            for x_cor in range(width):
                cell = self.board[y_cor][x_cor]
                norm_x = x_cor * self.cell_size
                norm_y = y_cor * self.cell_size

                if (x_cor, y_cor) in self.revealed:
                    if cell == "x":
                        self.mine_tiles.add(Mine(norm_x, norm_y))
                    elif cell == " ":
                        self.empty_tiles.add(Empty(norm_x, norm_y))
                    else:
                        self.adjecent_tiles.add(Adjecent(norm_x, norm_y, cell))
                else:
                    self.unrevealed_tiles.add(Unrevealed(norm_x, norm_y))

        self.all_sprites.add(
            self.mine_tiles,
            self.empty_tiles,
            self.adjecent_tiles,
            self.unrevealed_tiles
        )
