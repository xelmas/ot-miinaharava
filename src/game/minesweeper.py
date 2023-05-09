import pygame
from game.board import Board
from sprites.mine import Mine
from sprites.empty import Empty
from sprites.adjacent import Adjacent
from sprites.unrevealed import Unrevealed
from sprites.flag import Flag


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
        self._initialize_sprite_groups()

    def _initialize_sprite_groups(self):
        """Initialize the sprite groups.

        For each type of tile (mine, empty, adjacent, unrevealed, flagged) and all sprites 
        this method creates instances of the pygame sprite group class.
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

    def _initialize_sprites(self):
        """Initializes the sprite groups for each types of tiles and adds them to all_sprites group."""
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
        tile_position = (x_cor, y_cor)

        if tile_position in self.board.get_revealed():
            if tile_content == "x":
                self.mine_tiles.add(Mine(norm_x, norm_y))
            elif tile_content == " ":
                self.empty_tiles.add(Empty(norm_x, norm_y))
            elif isinstance(tile_content, int) and 1 <= tile_content <= 8:
                self.adjecent_tiles.add(Adjacent(norm_x, norm_y, tile_content))
        elif tile_position in self.board.get_flagged():
            self.flag_tiles.add(Flag(norm_x, norm_y))
        else:
            self.unrevealed_tiles.add(Unrevealed(norm_x, norm_y))

    def add_move(self):
        """Increases the count of moves made so far by 1."""
        self.board.add_move()

    def get_moves(self):
        """Returns the count of moves made so far.

        Returns:
            int: The count of moves made so far.
        """
        return self.board.get_moves()

    def get_game_mines(self):
        """Returns the number of mines on the board.

        Returns:
            int: The number of mines on the board.
        """
        return self.board.get_num_mines()

    def get_game_flagged(self):
        """Returns the number of tiles that are flagged.

        Returns:
            int: The number of tiles that are flagged.
        """
        return len(self.board.get_flagged())

    def get_game_mines_flagged_info(self):
        """Calculates the number of remaining mines to be flagged.

        The remaining number of mines is determined by subtracting the number of tiles flagged by the user from the total number of mines on the board.
        The count cannot be negative, even if the user flags more tiles than there are mines.
        If the user clicks the tile with the right mouse button, the tile will be flagged and the counter will be updated.

        Returns:
            int: The number of remaining mines on the board that are not flagged.
        """
        result = self.get_game_mines() - self.get_game_flagged()
        return max(result, 0)
