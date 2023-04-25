import random


class Board:
    def __init__(self, width, height, num_mines) -> None:
        self.width = width
        self.height = height
        self.num_mines = num_mines
        self.game_over = False

        self.mines = set()
        self.revealed = set()
        self.flagged = set()

        self.board = [["" for _ in range(self.width)]
                      for _ in range(self.height)]

        self.place_mines()

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

    def reveal(self, x_cor, y_cor):

        if x_cor < 0 or y_cor < 0:
            print("x and y cannot be negative")
            return False
        if x_cor >= self.width or y_cor >= self.height:
            print("Coordinate overflow")
            return False

        if (x_cor, y_cor) not in self.revealed:
            self.revealed.add((x_cor, y_cor))

        if (x_cor, y_cor) in self.mines:
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
                    self.reveal(x_cor2, y_cor2)
        else:
            self.board[y_cor][x_cor] = num_adjecent_mines

        return True

    def get_num_adjacent_mines(self, x_cor, y_cor):
        count = 0
        neighbors = self.get_neighbors(x_cor, y_cor)

        for x_cor2, y_cor2 in neighbors:
            if (x_cor2, y_cor2) in self.mines:
                count += 1
        return count

    def add_flag(self, x_cor, y_cor):
        if (x_cor, y_cor) not in self.flagged:
            self.flagged.add((x_cor, y_cor))
        else:
            self.remove_flag(x_cor, y_cor)

    def get_flagged(self):
        return self.flagged

    def remove_flag(self, x_cor, y_cor):
        self.flagged.remove((x_cor, y_cor))

    def get_revealed(self):
        return self.revealed

    def get_mines(self):
        return self.mines

    def get_num_mines(self):
        return self.num_mines

    def get_board(self):
        return self.board

    def get_is_game_over(self):
        return self.game_over

    def get_height(self):
        return self.height

    def get_width(self):
        return self.width
