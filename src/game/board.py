import random


class Board:
    """Representing a board for Minesweeper game.

    Attributes:
        mines(set): A set of coordinates of tiles containing mine.
        revealed(set): A set of coordinates of all revealed tiles.
        flagged(set): A set of coordinates of all flagged tiles.
        board(list): A 2-dimensional list representing the board.
        moves(int): The number of moves made so far.
    """

    def __init__(self, width, height, num_mines) -> None:
        """Initializes a Board object with given width, height and number of mines and places mines.

        Args:
            width (int): The width of the board.
            height (int): The height of the board.
            num_mines (int): The number of mines placed on the board.
        """
        self.width = width
        self.height = height
        self.num_mines = num_mines
        self.game_over = False
        self.moves = 0

        self.mines = set()
        self.revealed = set()
        self.flagged = set()

        self.board = [["" for _ in range(self.width)]
                      for _ in range(self.height)]

        self.place_mines()

    def place_mines(self):
        """Places mines randomly on the board."""
        for _ in range(self.num_mines):
            while True:
                x_cor = random.randint(0, self.width - 1)
                y_cor = random.randint(0, self.height - 1)

                if (x_cor, y_cor) not in self.mines:
                    self.mines.add((x_cor, y_cor))
                    self.board[y_cor][x_cor] = "x"
                    break

    def get_neighbors(self, x_cor, y_cor):
        """Determines the neighboring tiles of the given tile as a list of tuples (x_cor, y_cor).

        Args:
            x_cor (int): The x-coordinate of the tile.
            y_cor (int): The y-coordinate of the tile.

        Returns:
            list: The neighboring tiles of the given tile.
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

    def add_move(self):
        """Increases the count of moves made so far by 1."""
        self.moves += 1

    def get_moves(self):
        """Returns the count of moves made so far.

        Returns:
            int: The count of moves made so far.
        """
        return self.moves

    def reveal(self, x_cor, y_cor, click=1):
        """Reveals the content of the given tile on the board.

        Args:
            x_cor (int): The x-coordinate of the tile to reveal.
            y_cor (int): The y-coordinate of the tile to reveal.
            click (int): The number representing if the tile was clicked. Can be 1 or 0.
                         If the value is 1, moves counter will be increased by one.
                         If the value is 0, moves counter will be intact.

        Returns:
            bool: True if the tile was revealed succesfully, False otherwise.
        """
        tile_position = (x_cor, y_cor)

        if self.is_over_board(x_cor, y_cor):
            return False

        if tile_position not in self.revealed:
            self.revealed.add(tile_position)

            if click == 1:
                self.add_move()

        if tile_position in self.mines:
            self.game_over = True
            return False

        num_all_tiles = self.width * self.height - self.num_mines
        if len(self.revealed) == num_all_tiles:
            self.game_over = True
            return True

        num_adjecent_mines = self.get_num_adjacent_mines(x_cor, y_cor)
        if num_adjecent_mines == 0:
            self.board[y_cor][x_cor] = " "
            for x_cor2, y_cor2 in self.get_neighbors(x_cor, y_cor):
                if (x_cor2, y_cor2) not in self.revealed:
                    self.reveal(x_cor2, y_cor2, click=0)
        else:
            self.board[y_cor][x_cor] = num_adjecent_mines

        return True

    def get_num_adjacent_mines(self, x_cor, y_cor):
        """Count the number of adjacent mines for the given tile.

        Args:
            x_cor (int): The x-coordinate of the tile.
            y_cor (int): The y-coordinate of the tile.

        Returns:
            int: The number of adjacent mines.
        """
        count = 0
        neighbors = self.get_neighbors(x_cor, y_cor)

        for x_cor2, y_cor2 in neighbors:
            if (x_cor2, y_cor2) in self.mines:
                count += 1
        return count

    def is_over_board(self, x_cor, y_cor):
        """Checks if the clicked position is within the game board.

        Args:
            x_cor (int): The x-coordinate of the clicked position.
            y_cor (int): The y-coordinate of the clicked position.

        Returns:
            bool: True if the clicked position is outside of the game board,
                  False otherwise.
        """

        if x_cor < 0 or y_cor < 0:
            return True
        if x_cor >= self.width or y_cor >= self.height:
            return True
        return False

    def add_flag(self, x_cor, y_cor):
        """Adds or removes the given tile to/from the list of flagged tiles.

        If the tile is not flagged and the clicked position is within the game board, it will be added to the list.
        If the tile is already flagged, it will be removed from the list.

        Args:
            x_cor (int): The x-coordinate of the tile.
            y_cor (int): The y-coordinate of the tile.
        """
        tile_position = (x_cor, y_cor)
        if tile_position not in self.revealed and not self.is_over_board(x_cor, y_cor):
            if tile_position not in self.flagged:
                self.flagged.add(tile_position)
            else:
                self.remove_flag(x_cor, y_cor)

    def get_flagged(self):
        """Returns a set of all tiles that have been flagged.

        Returns:
            set: A set of tuples (x_cor, y_cor) of flagged tiles.
        """
        return self.flagged

    def remove_flag(self, x_cor, y_cor):
        """Removes the flag from given tile.

        Args:
            x_cor (int): The x-coordinate of the tile to remove the flag from.
            y_cor (int): The y-coordinate of the tile to remove the flag from.
        """
        self.flagged.remove((x_cor, y_cor))

    def get_revealed(self):
        """Returns a set of all tiles that have been revealed.

        Returns:
            set: A set of tuples (x_cor, y_cor) of revealed tiles.
        """
        return self.revealed

    def get_mines(self):
        """Returns the set of tiles that contain a mine.

        Returns:
            set: A set of tuples (x_cor, y_cor) representing
                 the coordinates of tiles containing a mine.
        """
        return self.mines

    def get_num_mines(self):
        """Returns the number of mines in the board.

        Returns:
            int: The number of mines in the board.
        """
        return self.num_mines

    def get_board(self):
        """Returns the current state of the board.

        Returns:
            list: A 2-dimensional list representing the state of the board.
        """
        return self.board

    def get_is_game_over(self):
        """Returns whether the game is over or not.

        Returns:
            bool: True if the game is over, False otherwise.
        """
        return self.game_over

    def get_height(self):
        """Returns the height of the board.

        Returns:
            int: The height of the board.
        """
        return self.height

    def get_width(self):
        """Returns the width of the board.

        Returns:
            int: The width of the board.
        """
        return self.width
