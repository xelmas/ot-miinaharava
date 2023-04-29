import pygame
from board import Board
from sprites.mine import Mine
from sprites.empty import Empty
from sprites.adjecent import Adjecent
from sprites.unrevealed import Unrevealed
from sprites.flag import Flag
from service.result_service import result_service


class Minesweeper:
    """A game of Minesweeper.

    Attributes:
        board (Board): The game board.
        time_passed (int): The time that has passed since the game started.
        cell_size (int): The size of one tile in pixels.
    """

    def __init__(self, width, height, num_mines, cell_size) -> None:
        """Create a new instance of Minesweeper.

        Args:
            width (int): The width of the game board.
            height (int): The height of the game board.
            num_mines (int): The number of mines to place on the board.
            cell_size (int): The size of one tile in pixels.
        """
        self.board = Board(width, height, num_mines)
        self.time_passed = 0
        self.cell_size = cell_size
        self._level = f"{width}, {height}, {num_mines}"
        self._initialize_sprite_groups()

    def _initialize_sprite_groups(self):
        """Initialize the sprite groups.

        For each type of tile (mine, empty, adjecent, unrevealed, flagged) and all sprites 
        this method creates instances of the Pygame sprite group class.
        Then it calls the _initialize_sprites() method 
        to create instances of each and add them to their groups.
        """
        self.mine_tiles = pygame.sprite.Group()
        self.empty_tiles = pygame.sprite.Group()
        self.adjecent_tiles = pygame.sprite.Group()
        self.unrevealed_tiles = pygame.sprite.Group()
        self.flag_tiles = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        self._initialize_sprites()

    def show_mines(self):
        """Reveals all tiles containing mines by adding them to the revealed list."""
        for x_cor, y_cor in self.board.get_mines():
            self.board.get_revealed().add((x_cor, y_cor))

    def save_result(self):
        result_service.create_result(
            "PLAYER", self._level, self.time_passed, self.board.get_moves())
        self.print_results()

    def print_results(self):
        results = result_service.get_results()
        for stat in results:
            print("name:", stat.username, "\nlevel (w, h, m):",
                  stat.level, "\ntime (s):", stat.time, "\nmoves:", stat.moves)
            print()

    def is_won(self):
        """Checks if the game has been won. 

        If all non-mine tiles are revealed, the method will reveal all remaining tiles
        by calling show_mines() method, and returns True.

        Returns:
            bool: True if the game is won, False otherwise.
        """
        num_all_tiles = self.board.width * self.board.height - self.board.num_mines
        if len(self.board.get_revealed()) == num_all_tiles:
            self.show_mines()
            return True
        return False

    def is_lost(self):
        """Checks if the game is lost. 

        If the game is over, the method will reveal all mines 
        by calling show_mines() method, and returns True.

        Returns:
            bool: True if the game is lost, False otherwise.
        """
        if self.board.get_is_game_over():
            self.show_mines()
            return True
        return False

    def update_game(self, display):
        """Updates the state of the game on the display.

        Args:
            display (pygame.Surface): The surface to draw on to.
        """
        self._initialize_sprites()
        self.all_sprites.draw(display)
        pygame.display.update()

    def _initialize_sprites(self):
        """Initialize the sprite groups for each types of tiles
           and add them to all_sprites group.
        """
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
        """Initializes a sprite for a tile on the board based on the content.

        Args:
            x_cor (int): The x-coordinate of the tile.
            y_cor (int): The y-coordinate of the tile.
            tile_content (str or int): The content of the tile. Can be string if the content 
                                       is a mine, empty or flagged tile or an integer 
                                       if there is at least one mine nearby.
        """
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
        """Sets time that has passed since the start of the game.

        Args:
            time_passed_seconds (int): The time that has passed in seconds.
        """
        self.time_passed = time_passed_seconds

    def get_time_passed(self):
        """Returns the time that has passed since the start of the game.

        Returns:
            int: The time that has passed in seconds.
        """
        return self.time_passed

    def add_move(self):
        """Increases the count of moves made so far by 1."""
        self.board.add_move()

    def get_moves(self):
        """Returns the count of moves made so far.

        Returns:
            int: The count of moves made so far.
        """
        return self.board.get_moves()
