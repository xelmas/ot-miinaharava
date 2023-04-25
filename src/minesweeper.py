import pygame
from board import Board
from sprites.mine import Mine
from sprites.empty import Empty
from sprites.adjecent import Adjecent
from sprites.unrevealed import Unrevealed
from sprites.flag import Flag


class Minesweeper:

    def __init__(self, width, height, num_mines, cell_size) -> None:
        self.board = Board(width, height, num_mines)
        self.moves = 0
        self.time_passed = 0
        self.cell_size = cell_size
        self._initialize_sprite_groups()

    def _initialize_sprite_groups(self):
        self.mine_tiles = pygame.sprite.Group()
        self.empty_tiles = pygame.sprite.Group()
        self.adjecent_tiles = pygame.sprite.Group()
        self.unrevealed_tiles = pygame.sprite.Group()
        self.flag_tiles = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        self._initialize_sprites()

    def show_mines(self):
        for x_cor, y_cor in self.board.get_mines():
            self.board.get_revealed().add((x_cor, y_cor))

    def is_won(self):
        num_all_tiles = self.board.width * self.board.height - self.board.num_mines
        if len(self.board.get_revealed()) == num_all_tiles:
            self.show_mines()
            return True
        return False

    def is_lost(self):
        if self.board.get_is_game_over():
            self.show_mines()
            return True
        return False

    def update_game(self, display):
        self._initialize_sprites()
        self.all_sprites.draw(display)
        pygame.display.update()

    def _initialize_sprites(self):
        for y_cor, row in enumerate(self.board.get_board()):
            for x_cor, tile_content in enumerate(row):
                self._initialize_tile_sprite(x_cor, y_cor, tile_content)

        self.all_sprites.add(
            self.mine_tiles,
            self.empty_tiles,
            self.adjecent_tiles,
            self.unrevealed_tiles,
            self.flag_tiles
        )

    def _initialize_tile_sprite(self, x_cor, y_cor, tile_content):
        norm_x = x_cor * self.cell_size
        norm_y = y_cor * self.cell_size
        if (x_cor, y_cor) in self.board.get_revealed():
            if tile_content == "x":
                self.mine_tiles.add(Mine(norm_x, norm_y))
            elif tile_content == " ":
                self.empty_tiles.add(Empty(norm_x, norm_y))
            elif tile_content in [1, 2, 3, 4, 5, 6, 7, 8]:
                self.adjecent_tiles.add(Adjecent(norm_x, norm_y, tile_content))
        elif (x_cor, y_cor) in self.board.get_flagged():
            self.flag_tiles.add(Flag(norm_x, norm_y))
        else:
            self.unrevealed_tiles.add(Unrevealed(norm_x, norm_y))

    def set_time_passed(self, time_passed_seconds):
        self.time_passed = time_passed_seconds

    def get_time_passed(self):
        return self.time_passed

    def add_move(self):
        self.moves += 1

    def get_moves(self):
        return self.moves
