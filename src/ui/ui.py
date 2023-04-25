import pygame_gui
import pygame
from minesweeper import Minesweeper

LEVELS = {"Beginner": (9, 9, 10), "Intermediate": (
    16, 16, 40), "Expert": (16, 30, 99), "Custom": (15, 15, 15)}
CELL_SIZE = 31


class UI:
    def __init__(self) -> None:
        pygame.init()
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Main menu")
        self.window_surface = pygame.display.set_mode((800, 600))

        self.background = pygame.Surface((800, 600))
        self.background.fill(pygame.Color('#000000'))
        self.manager = pygame_gui.UIManager((800, 600))
        self.level = "Beginner"
        self.create_buttons()
        self.set_level()

    def create_buttons(self):
        self.play_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 200), (120, 50)),
                                                        text="Play",
                                                        manager=self.manager, visible=0)
        self.options_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 250), (120, 50)),
                                                           text="Options",
                                                           manager=self.manager, visible=0)
        self.to_menu_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((100, 100), (120, 50)),
                                                           text="Main Menu",
                                                           manager=self.manager, visible=0)
        self.leaderboard_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 200+100), (120, 50)),
                                                               text="Leaderboard",
                                                               manager=self.manager, visible=0)
        self.credits_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 200+150), (120, 50)),
                                                           text="Credits",
                                                           manager=self.manager, visible=0)

        self.quit_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 200+200), (120, 50)),
                                                        text="Quit",
                                                        manager=self.manager, visible=0)

    def main_menu(self):

        pygame.display.set_caption("Main menu")
        self.play_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 200), (150, 50)),
                                                        text="Play",
                                                        manager=self.manager)
        self.options_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 250), (150, 50)),
                                                           text="Options",
                                                           manager=self.manager)
        self.leaderboard_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 200+100), (150, 50)),
                                                               text="Leaderboard",
                                                               manager=self.manager, visible=1)
        self.credits_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 200+150), (150, 50)),
                                                           text="Credits",
                                                           manager=self.manager, visible=1)

        self.quit_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 200+200), (150, 50)),
                                                        text="Quit",
                                                        manager=self.manager, visible=1)

    def options(self):
        self.manager.clear_and_reset()
        pygame.display.set_caption("Options")
        pygame_gui.elements.UILabel(relative_rect=pygame.Rect(
            (350, 150), (120, 70)), text="Choose level", manager=self.manager)
        pygame_gui.elements.UIDropDownMenu(options_list=[
            "Beginner", "Intermediate", "Expert", "Custom"], starting_option=self.level, relative_rect=pygame.Rect((350, 200), (150, 50)))

        if self.level == "Custom":
            pygame_gui.elements.UILabel(relative_rect=pygame.Rect(
                (45, 240), (290, 70)), text="Give width (number) and press enter:", manager=self.manager)

            pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((350, 250), (150, 50)),
                                                manager=self.manager, placeholder_text=f"{self.game_width}", visible=1, object_id="width")
            pygame_gui.elements.UILabel(relative_rect=pygame.Rect(
                (45, 290), (300, 70)), text="Give height (number) and press enter:", manager=self.manager)
            pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((350, 250+50), (150, 50)),
                                                manager=self.manager, placeholder_text=f"{self.game_height}", visible=1, object_id="height")

            pygame_gui.elements.UILabel(relative_rect=pygame.Rect(
                (45, 340), (290, 70)), text="Give mines (number) and press enter:", manager=self.manager)

            pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((350, 250+100), (150, 50)),
                                                manager=self.manager, placeholder_text=f"{self.game_mines}", visible=1, object_id="mines")

        self.to_menu_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((90, 50), (200, 40)),
                                                           text="To main menu",
                                                           manager=self.manager, visible=1)
        self.set_level()

    def credits(self):
        self.manager.clear_and_reset()
        pygame.display.set_caption("Credits")
        pygame_gui.elements.UILabel(relative_rect=pygame.Rect(
            (350, 100), (120, 70)), text="Credits", manager=self.manager)

        pygame_gui.elements.UILabel(relative_rect=pygame.Rect(
            (50, 110), (650, 200)), text="Icons by Lorc (https://lorcblog.blogspot.com) under CC BY 3.0 via game-icons.net", manager=self.manager)
        pygame_gui.elements.UILabel(relative_rect=pygame.Rect(
            (50, 140), (466, 200)), text="Game by xelmas (https://github.com/xelmas/ot-miinaharava)", manager=self.manager)

        self.to_menu_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((90, 50), (200, 40)),
                                                           text="To main menu",
                                                           manager=self.manager, visible=1)

    def draw_timer_and_counter(self, display, time_passed_seconds, game):
        font = pygame.font.SysFont(None, 35)
        text_hide_prev_num = pygame.Rect(32 * self.game_width, 10, 200, 50)
        pygame.draw.rect(display, (0, 0, 0), text_hide_prev_num)
        text_hide_prev_num = pygame.Rect(32 * self.game_width, 40, 200, 50)
        pygame.draw.rect(display, (0, 0, 0), text_hide_prev_num)

        text = font.render(
            f"Time: {time_passed_seconds}", True, (255, 255, 255))
        display.blit(text, (32 * self.game_width, 10))
        text = font.render(
            f"Moves: {game.get_moves()}", True, (255, 255, 255))
        display.blit(text, (32 * self.game_width, 40))

    def draw_game_over_info_won(self, display):
        font = pygame.font.SysFont(None, 32)
        text = font.render(
            f"You won!", True, (255, 255, 255))
        display.blit(text, (20, 32*self.game_height))

    def draw_game_over_info_lost(self, display):
        font = pygame.font.SysFont(None, 32)
        text = font.render(
            f"You lose", True, (255, 255, 255))
        display.blit(text, (20, 32*self.game_height))

    def handle_game_events(self, game, display, time_passed_seconds):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_over = True
                pygame.quit()
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x_cor, y_cor = pygame.mouse.get_pos()
                x_cor = x_cor // game.cell_size
                y_cor = y_cor // game.cell_size

                if event.button == 1:  # left click
                    game.board.reveal(x_cor, y_cor)
                    game.add_move()
                    game.update_game(display)
                    pygame.display.update()
                    if game.is_won():
                        game.set_time_passed(time_passed_seconds)
                        print("time passed:",
                              game.get_time_passed(), "second(s)")
                        self.draw_game_over_info_won(display)
                        game.update_game(display)
                        self.game_over = True

                        pygame.time.wait(1000)

                    elif game.is_lost():
                        game.set_time_passed(time_passed_seconds)
                        print("time passed:",
                              game.get_time_passed(), "second(s)")
                        self.draw_game_over_info_lost(display)
                        game.update_game(display)
                        self.game_over = True
                        pygame.time.wait(1000)

                elif event.button == 3:  # right click
                    game.board.add_flag(x_cor, y_cor)
                    game.update_game(display)

    def initialize_game_window(self):
        display_height = self.game_height * CELL_SIZE + 200
        display_width = self.game_width * CELL_SIZE + 200
        display = pygame.display.set_mode((display_width, display_height))
        pygame.display.set_caption("Minesweeper")
        pygame.init()
        return display

    def start(self):
        display = self.initialize_game_window()
        game = Minesweeper(self.game_width, self.game_height,
                           self.game_mines, CELL_SIZE)
        # initialize timer
        timer = pygame.time.Clock()
        start_time = pygame.time.get_ticks()
        game.all_sprites.draw(display)
        self.game_over = False

        while not self.game_over:
            time_passed = pygame.time.get_ticks() - start_time
            time_passed_seconds = round(time_passed / 1000)
            self.draw_timer_and_counter(display, time_passed_seconds, game)
            self.handle_game_events(game, display, time_passed_seconds)
            pygame.display.update()
            timer.tick(60)

    def handle_text_entry(self, event):
        if event.ui_object_id == "width":
            width = event.text
            if str(width).isdigit() and int(width) > 0:
                self.set_game_width(int(width))
        if event.ui_object_id == "height":
            height = event.text
            if str(height).isdigit() and int(height) > 0:
                self.set_game_height(int(height))
        if event.ui_object_id == "mines":
            mines = event.text
            if str(mines).isdigit() and int(mines) > 0:
                self.set_game_mines(int(mines))

    def handle_menu_change(self, event):
        self.level = event.text
        self.options()

    def handle_menu_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False

            elif event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == self.play_button:
                    self.start()
                    exit()
                if event.ui_element == self.options_button:
                    self.options()
                if event.ui_element == self.to_menu_button:
                    self.manager.clear_and_reset()
                    self.main_menu()
                if event.ui_element == self.leaderboard_button:
                    pass
                if event.ui_element == self.credits_button:
                    self.credits()
                if event.ui_element == self.quit_button:
                    self.is_running = False

            elif event.type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED:
                self.handle_menu_change(event)

            elif event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and self.level == "Custom":
                self.handle_text_entry(event)

            self.manager.process_events(event)

    def menu_loop(self):
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
        self.game_width, self.game_height, self.game_mines = LEVELS[self.level]

    def set_game_width(self, game_width):
        self.game_width = game_width

    def set_game_height(self, game_height):
        self.game_height = game_height

    def set_game_mines(self, game_mines):
        self.game_mines = game_mines
