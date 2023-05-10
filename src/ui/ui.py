import pygame_gui
import pygame
from game.minesweeper import Minesweeper
from service.result_service import result_service

LEVELS = {"Beginner": (9, 9, 10), "Intermediate": (
    16, 16, 40), "Expert": (16, 30, 99), "Custom": (15, 15, 15)}
CELL_SIZE = 31
FONT_PATH = "src/assets/font/RationalInteger.ttf"


class UI:
    """User Interface of the game Minesweeper.

    Attributes:
        clock: pygame.time.Clock object for tracking game time.
        window_surface: pygame.Surface object represents the game window.
        background: pygame.Surface object represents the game background.
        manager: pygame_gui.UIManager object for managing the game UI.
        level: The string representing the current game level, 
               can be "Beginner, "Intermediate", "Expert" or "Custom".
        username: The string representing the player name, default "PLAYER".
    """

    def __init__(self) -> None:
        """Initializes the game UI window.

        Sets up the game window and background, creates the pygame-gui manager,
        sets starting level to "Beginner" and sets the default username to "PLAYER".
        """
        pygame.init()
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Main menu")
        self.window_surface = pygame.display.set_mode((800, 600))

        self.background = pygame.Surface((800, 600))
        self.background.fill(pygame.Color('#000000'))
        self.manager = pygame_gui.UIManager((800, 600))
        self.level = "Beginner"
        self.username = "PLAYER"
        self.set_level()

    def main_menu(self):
        """Initializes and displays the main menu of the game with pygame-gui buttons.

        The buttons include options to play the game, access options, view the leaderboard, view credits, and quit the game.
        It also creates a hidden back to menu button, which will be set visible later.
        """
        self.play_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((320, 200), (150, 50)),
                                                        text="Play",
                                                        manager=self.manager)
        self.options_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((320, 250), (150, 50)),
                                                           text="Options",
                                                           manager=self.manager)
        self.leaderboard_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((320, 200+100), (150, 50)),
                                                               text="Leaderboard",
                                                               manager=self.manager, visible=1)
        self.credits_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((320, 200+150), (150, 50)),
                                                           text="Credits",
                                                           manager=self.manager, visible=1)

        self.quit_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((320, 200+200), (150, 50)),
                                                        text="Quit",
                                                        manager=self.manager, visible=1)
        self.to_menu_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((100, 100), (120, 50)),
                                                           text="Main Menu",
                                                           manager=self.manager, visible=0)

    def options(self):
        """Displays the view, where the user can select the difficulty level and give a username.

        The available levels to choose from are Beginner, Intermediate, Expert and Custom. 
        If the user selects the Custom, additional input fields appear for the user to give the width,
        height and number of mines for the game.

        The selected options are stored in the attributes:
        - self.level
        - self.game_width
        - self.game_height
        - self.game_mines
        - self.username

        To go back to the main menu, the user can click on the "To main menu" button.
        """
        self.manager.clear_and_reset()
        pygame.display.set_caption("Options")

        pygame_gui.elements.UILabel(relative_rect=pygame.Rect(
            (90, 100), (340, 70)), text="Type into box and press enter to confirm.", manager=self.manager)

        pygame_gui.elements.UILabel(relative_rect=pygame.Rect(
            (465, 150), (250, 70)), text="Give name (3-10 characters)", manager=self.manager)

        pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((480, 200), (150, 50)),
                                            manager=self.manager, placeholder_text=f"{self.username}", visible=1, object_id="username")
        pygame_gui.elements.UILabel(relative_rect=pygame.Rect(
            (240, 150), (120, 70)), text="Choose level", manager=self.manager)
        pygame_gui.elements.UIDropDownMenu(options_list=[
            "Beginner", "Intermediate", "Expert", "Custom"], starting_option=self.level, relative_rect=pygame.Rect((250, 200), (150, 50)))

        if self.level == "Custom":
            pygame_gui.elements.UILabel(relative_rect=pygame.Rect(
                (70, 240), (300, 70)), text="Width:", manager=self.manager)

            pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((250, 250), (150, 50)),
                                                manager=self.manager, placeholder_text="15", visible=1, object_id="width")
            pygame_gui.elements.UILabel(relative_rect=pygame.Rect(
                (70, 290), (300, 70)), text="Height:", manager=self.manager)
            pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((250, 250+50), (150, 50)),
                                                manager=self.manager, placeholder_text="15", visible=1, object_id="height")

            pygame_gui.elements.UILabel(relative_rect=pygame.Rect(
                (70, 340), (300, 70)), text="Mines:", manager=self.manager)

            pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((250, 250+100), (150, 50)),
                                                manager=self.manager, placeholder_text="15", visible=1, object_id="mines")

            pygame_gui.elements.UILabel(relative_rect=pygame.Rect(
                (68, 200), (672, 500)), text="The width, height, and number of mines must be positive integers, with the width and", manager=self.manager)

            pygame_gui.elements.UILabel(relative_rect=pygame.Rect(
                (68, 220), (664, 500)), text="height being at least 5 and the number of mines between 2 and 300. If the number of", manager=self.manager)

            pygame_gui.elements.UILabel(relative_rect=pygame.Rect(
                (68, 240), (664, 500)), text="mines is outside this range, the default value of 15 will be applied. If either the", manager=self.manager)

            pygame_gui.elements.UILabel(relative_rect=pygame.Rect(
                (68, 260), (672, 500)), text="width or height exceeds 32, the default value of 15 will also be applied. Otherwise,", manager=self.manager)
            pygame_gui.elements.UILabel(relative_rect=pygame.Rect(
                (68, 280), (560, 500)), text="the entered width and height, and number of mines values will be used.", manager=self.manager)

        self.to_menu_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((90, 50), (200, 40)),
                                                           text="To main menu",
                                                           manager=self.manager, visible=1)
        self.set_level()

    def show_leaderboard(self):
        """Displays the leaderboard with the top 10 scores.

        Calls the result service and displays the player name, game level, time and moves of the top 10 scores
        of the retrieved data.

        To go back to the main menu, the user can click on the "To main menu" button.
        """

        self.manager.clear_and_reset()
        pygame.display.set_caption("Leaderboard")
        pygame_gui.elements.UILabel(relative_rect=pygame.Rect(
            (100, 80), (365, 100)), text="Displaying only the games that have been won.", manager=self.manager)
        pygame_gui.elements.UILabel(relative_rect=pygame.Rect(
            (100, 80), (600, 150)), text="Level parameters corresponds to the game width, height and number of mines.", manager=self.manager)

        pygame_gui.elements.UILabel(relative_rect=pygame.Rect(
            (350, 130), (100, 100)), text="Leaderboard", manager=self.manager)

        padding = 50
        pygame_gui.elements.UILabel(relative_rect=pygame.Rect(
            (100, 120), (300, 200)), text="Name", manager=self.manager)
        pygame_gui.elements.UILabel(relative_rect=pygame.Rect(
            (250, 120), (300, 200)), text="Level (w, h, m)", manager=self.manager)
        pygame_gui.elements.UILabel(relative_rect=pygame.Rect(
            (400, 120), (300, 200)), text="Time (s)", manager=self.manager)
        pygame_gui.elements.UILabel(relative_rect=pygame.Rect(
            (500, 120), (300, 200)), text="Moves", manager=self.manager)

        results = result_service.get_top_ten()
        for stat in results:
            pygame_gui.elements.UILabel(relative_rect=pygame.Rect(
                (100, 120), (300, 200+padding)), text=f"{stat.username}", manager=self.manager)
            pygame_gui.elements.UILabel(relative_rect=pygame.Rect(
                (250, 120), (300, 200+padding)), text=f"{stat.level}", manager=self.manager)
            pygame_gui.elements.UILabel(relative_rect=pygame.Rect(
                (400, 120), (300, 200+padding)), text=f"{stat.time}", manager=self.manager)
            pygame_gui.elements.UILabel(relative_rect=pygame.Rect(
                (500, 120), (300, 200+padding)), text=f"{stat.moves}", manager=self.manager)
            padding += 50

        self.to_menu_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((90, 50), (200, 40)),
                                                           text="To main menu",
                                                           manager=self.manager, visible=1)

    def credits(self):
        """Displays the credits view with the information about the game and icons used.

        Creates two labels with the credits information and a button to return to the main menu.
        """
        self.manager.clear_and_reset()
        pygame.display.set_caption("Credits")
        pygame_gui.elements.UILabel(relative_rect=pygame.Rect(
            (340, 100), (120, 70)), text="Credits", manager=self.manager)

        pygame_gui.elements.UILabel(relative_rect=pygame.Rect(
            (50, 110), (650, 200)), text="Icons by Lorc (https://lorcblog.blogspot.com) under CC BY 3.0 via game-icons.net", manager=self.manager)
        pygame_gui.elements.UILabel(relative_rect=pygame.Rect(
            (50, 140), (466, 200)), text="Game by xelmas (https://github.com/xelmas/ot-miinaharava)", manager=self.manager)

        self.to_menu_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((90, 50), (200, 40)),
                                                           text="To main menu",
                                                           manager=self.manager, visible=1)

    def draw_timer_and_counters(self, display, time_passed_seconds, game):
        """Draws the game timer, moves and remaining mines counter on the screen.

        Args:
            display (pygame.Surface): The surface to draw the timer and counter on.
            time_passed_seconds (int): The time passed in seconds.
            game (Minesweeper): An instance of the Minesweeper class representing the game.
        """
        font = pygame.font.Font(FONT_PATH, 28)
        text_hide_prev_clock = pygame.Rect(32 * self.game_width, 10, 200, 50)
        pygame.draw.rect(display, (0, 0, 0), text_hide_prev_clock)
        text_hide_prev_moves = pygame.Rect(32 * self.game_width, 40, 200, 50)
        pygame.draw.rect(display, (0, 0, 0), text_hide_prev_moves)
        text_hide_prev_mines = pygame.Rect(32 * self.game_width, 70, 200, 50)
        pygame.draw.rect(display, (0, 0, 0), text_hide_prev_mines)

        text = font.render(
            f"Time: {time_passed_seconds}", True, (255, 255, 255))
        display.blit(text, (32 * self.game_width + 30, 10))
        text = font.render(
            f"Moves: {game.get_moves()}", True, (255, 255, 255))
        display.blit(text, (32 * self.game_width + 30, 40))
        text = font.render(
            f"Mines: {game.get_game_mines_flagged_info()}", True, (255, 255, 255))
        display.blit(text, (32 * self.game_width + 30, 70))

    def draw_game_over_info_won(self, display):
        """Draws "You won!" on the screen if the game has been won.

        If the game has not been won, this function should not be called.

        Args:
            display (pygame.Surface): The surface to draw on to.
        """
        font = pygame.font.Font(FONT_PATH, 30)
        text = font.render(
            f"You won!", True, (0, 255, 0))
        display.blit(text, (32 * self.game_width + 30, 123))

    def draw_game_over_info_lost(self, display):
        """Draws "You lose" on the screen if the game has been lost.

        If the game has not been lost, this function should not be called.

        Args:
            display (pygame.Surface): The surface to draw on to.
        """
        font = pygame.font.Font(FONT_PATH, 30)
        text = font.render(
            f"You lose", True, (255, 0, 0))
        display.blit(text, (32 * self.game_width + 30, 123))

    def save_result(self, time_passed_seconds, moves):
        """Saves the player's score with their username, game level, time and number of moves.

        Calls the result service and saves the score with the player's name, the game level they played,
        the time passed from the start of the game and the number of moves made during the game.

        Args:
            time_passed_seconds (int): The time passed in seconds from the start of the game.
            moves (int): The number of moves made in the game.
        """
        result_service.create_result(
            self.username, self.get_level(), time_passed_seconds, moves)

    def handle_game_events(self, game, display, time_passed_seconds):
        """Handle the events that happen during the game.

        The method updates the game board based on the events triggered by the user.
        If the user clicks on a cell with the left mouse button, the cell is revealed.
        If the user clicks on a cell with the right mouse button, the tile is flagged.
        If the user wins or loses the game, corresponding message is displayed and the score is saved (if won).

        Args:
            game (Minesweeper): The current game.
            display (pygame.Surface): The display to update.
            time_passed_seconds (int): The time passed in seconds.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_over = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x_cor, y_cor = pygame.mouse.get_pos()
                x_cor = x_cor // game.cell_size
                y_cor = y_cor // game.cell_size

                if event.button == 1:  # left click
                    game.board.reveal(x_cor, y_cor)
                    self.update_game(display, game)
                    pygame.display.update()
                    if game.is_won():
                        self.draw_game_over_info_won(display)
                        self.save_result(time_passed_seconds,
                                         game.get_moves())
                        self.update_game(display, game)
                        self.game_over = True
                        pygame.time.wait(2000)

                    elif game.is_lost():
                        self.draw_game_over_info_lost(display)
                        self.update_game(display, game)
                        self.game_over = True
                        pygame.time.wait(2000)

                elif event.button == 3:  # right click
                    game.board.add_flag(x_cor, y_cor)
                    self.update_game(display, game)

    def initialize_game_window(self):
        """Initializes the game window for the Minesweeper.

        Creates and returns a pygame display representing the game window. The display size is determined by
        multiplying the game board dimensions (in tiles) by the size of cell, and adding 200 pixels to width for padding.
        Pygame is initialized and the game window caption is set to "Minesweeper".

        Returns:
            pygame.Surface: The display representing the game window for Minesweeper.
        """
        display_height = self.game_height * CELL_SIZE
        display_width = self.game_width * CELL_SIZE + 200
        display = pygame.display.set_mode((display_width, display_height))
        pygame.display.set_caption("Minesweeper")
        return display

    def update_game(self, display, game):
        """Updates the state of the game on the display.

        Args:
            display (pygame.Surface): The surface to draw on to.
            game (Minesweeper): The current game.
        """
        game._initialize_sprites()
        game.all_sprites.draw(display)
        pygame.display.update()

    def start(self):
        """Starts the Minesweeper game.

        Initializes the game window, creates a new Minesweeper game, 
        initializes the timer and counters, and starts the game loop.
        The game window is displayed until the user quits or the game ends.
        """
        game_window = self.initialize_game_window()
        game = Minesweeper(self.game_width, self.game_height,
                           self.game_mines, CELL_SIZE)

        timer = pygame.time.Clock()
        start_time = pygame.time.get_ticks()
        game.all_sprites.draw(game_window)
        self.game_over = False

        while not self.game_over:
            time_passed = pygame.time.get_ticks() - start_time
            time_passed_seconds = round(time_passed / 1000)
            self.draw_timer_and_counters(
                game_window, time_passed_seconds, game)
            self.handle_game_events(game, game_window, time_passed_seconds)
            pygame.display.update()
            timer.tick(60)
        pygame.display.quit()

    def handle_text_entry(self, event):
        """Handle the text entries in the options view. 

        Method handles user input from text boxes in the options view.
        It sets the game's parameters (width, height, mines) or the player's name
        depending on which text box was triggered.

        Args:
            event (pygame.event): The event that triggered the text entry.
        """
        if event.ui_object_id == "width":
            width = event.text
            if str(width).isdigit() and 32 >= int(width) >= 5:
                self.set_game_width(int(width))
        if event.ui_object_id == "height":
            height = event.text
            if str(height).isdigit() and 32 >= int(height) >= 5:
                self.set_game_height(int(height))
        if event.ui_object_id == "mines":
            mines = event.text
            if str(mines).isdigit() and 300 >= int(mines) >= 2 and self.game_height*self.game_height - int(mines) >= 1:
                self.set_game_mines(int(mines))
        if event.ui_object_id == "username":
            username = event.text
            if 10 >= len(username) >= 3:
                self.set_username(username)

    def handle_menu_change(self, event):
        """Handle a change in the dropdown menu in the options view.

        Method sets "self.level" parameter to the selected level.

        Args:
            event (pygame.event): The event that triggered the dropdown menu change.
                                  The "text" attribute contain the text of the selected level.
        """
        self.level = event.text
        self.options()

    def to_main_menu(self):
        """Clears the display, sets the window caption to Main Menu and switches to main menu view."""
        self.manager.clear_and_reset()
        pygame.display.set_caption("Main Menu")
        self.main_menu()

    def start_game(self):
        """Starts the new game and switches to the game view.

        The start() method initializes the game and displays the game window.
        Once the game is over, it will set the window back to its original size
        and the view is switched back to the main menu.
        """
        self.start()
        self.window_surface = pygame.display.set_mode((800, 600))
        self.to_main_menu()

    def handle_menu_events(self):
        """Handle the events triggered in the game menu.

        Method handles different types of events, clicking on a button, text entry 
        or changing the value of a dropdown menu. Then it calls the specific method to handle the event.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False

            elif event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == self.play_button:
                    self.start_game()
                if event.ui_element == self.options_button:
                    self.options()
                if event.ui_element == self.to_menu_button:
                    self.to_main_menu()
                if event.ui_element == self.leaderboard_button:
                    self.show_leaderboard()
                if event.ui_element == self.credits_button:
                    self.credits()
                if event.ui_element == self.quit_button:
                    self.is_running = False

            elif event.type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED:
                self.handle_menu_change(event)

            elif event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED:
                self.handle_text_entry(event)

            self.manager.process_events(event)

    def menu_loop(self):
        """Creates the main menu and starts the menu loop.

        In the each cycle of loop, the method handles events, updates the UI-manager
        and draws the UI on the window. The loop continues until the "is_running" value is set to "False". 
        This happens if the user clicks the "Quit" button.
        """
        self.main_menu()
        self.is_running = True

        while self.is_running:
            time_delta = self.clock.tick(60)/1000.0
            self.handle_menu_events()
            self.manager.update(time_delta)
            self.window_surface.blit(self.background, (0, 0))
            self.manager.draw_ui(self.window_surface)

            pygame.display.update()

    def set_level(self):
        """Sets the game level based on the current value of "self.level".

        Updates the "game_width", "game_height" and "game_mines" attributes 
        based on the values defined in the "LEVELS" dictionary constant.
        """
        self.game_width, self.game_height, self.game_mines = LEVELS[self.level]

    def get_level(self):
        """Returns a string representing the current game level.

        The level is determined by the width, height and the number of mines of the game.

        Returns:
            str: The current game level in the format "width, height, mines".
        """
        return f"{self.game_width}, {self.game_height}, {self.game_mines}"

    def set_game_width(self, game_width):
        """Sets the width of the game board in tiles.

        Represents the number of columns on the board. Must be an integer greater than 0.

        Args:
            game_width (int): The width of the game board in tiles.
        """
        self.game_width = game_width

    def set_game_height(self, game_height):
        """Sets the height of the game board in tiles.

        Represents the number of rows on the board. Must be an integer greater than 0.

        Args:
            game_height (int): The height of the game board in tiles.
        """
        self.game_height = game_height

    def set_game_mines(self, game_mines):
        """Sets the number of mines on the board.

        Args:
            game_mines (int): The number of mines on the board.
        """
        self.game_mines = game_mines

    def set_username(self, username):
        """Sets the given username for the player's name.

        The username will be used when the score is saved.

        Args:
            username (str): The player's name.
        """
        self.username = username

    def get_username(self):
        """Returns the player's name.

        Returns:
            str: The player's name.
        """
        return self.username
