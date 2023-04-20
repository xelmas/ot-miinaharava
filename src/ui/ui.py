import pygame_gui
import pygame
from minesweeper import Minesweeper

LEVELS = {"Beginner": (9, 9, 10), "Intermediate": (
    16, 16, 40), "Expert": (16, 30, 99), "Custom": (15, 15, 15)}
CELL_SIZE = 41


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

    def set_level(self):
        self.game_width, self.game_height, self.game_mines = LEVELS[self.level]

    def get_level_parameters(self):
        return "width", self.game_width, "height", self.game_height, "mines", self.game_mines

    def get_level(self):
        return self.level

    def set_game_width(self, game_width):
        self.game_width = game_width

    def set_game_height(self, game_height):
        self.game_height = game_height

    def set_game_mines(self, game_mines):
        self.game_mines = game_mines

    def get_game_width(self):
        return self.game_width

    def get_game_height(self):
        return self.game_height

    def get_game_mines(self):
        return self.game_mines

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
                (70, 240), (300, 70)), text="Write number and press enter:", manager=self.manager)
            pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((350, 250), (150, 50)),
                                                manager=self.manager, placeholder_text=f"{self.game_width}", visible=1, object_id="width")
            pygame_gui.elements.UILabel(relative_rect=pygame.Rect(
                (70, 290), (300, 70)), text="Write number and press enter:", manager=self.manager)

            pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((350, 250+50), (150, 50)),
                                                manager=self.manager, placeholder_text=f"{self.game_height}", visible=1, object_id="height")
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
                (70, 110), (500, 200)), text="Icons by Lorc (https://lorcblog.blogspot.com) under CC BY 3.0", manager=self.manager)
        pygame_gui.elements.UILabel(relative_rect=pygame.Rect(
                (70, 140), (466, 200)), text="Game by xelmas (https://github.com/xelmas/ot-miinaharava)", manager=self.manager)

        self.to_menu_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((90, 50), (200, 40)),
                                                           text="To main menu",
                                                           manager=self.manager, visible=1)
    def start(self):
        display_height = self.game_height * CELL_SIZE
        display_width = self.game_width * CELL_SIZE
        display = pygame.display.set_mode((display_width, display_height))
        pygame.display.set_caption("Minesweeper")
        game = Minesweeper(self.game_width, self.game_height,
                           self.game_mines, CELL_SIZE)
        pygame.init()
        game.all_sprites.draw(display)

        running = True
        print("level", self.get_level_parameters())

        while running:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    return
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x_cor, y_cor = pygame.mouse.get_pos()
                    x_cor = x_cor // game.cell_size
                    y_cor = y_cor // game.cell_size

                    if event.button == 1:  # left click
                        game.reveal(x_cor, y_cor)
                        game._initialize_sprites()
                        game.all_sprites.draw(display)
                        pygame.display.update()
                        if game.game_over:
                            print("you lose")
                            pygame.time.wait(1000)
                            return

                    if event.button == 3:  # right click
                        game.add_flag(x_cor, y_cor)
                        game._initialize_sprites()
                        game.all_sprites.draw(display)
                        pygame.display.update()

                        if game.game_over:
                            print("you won")
                            pygame.time.wait(1000)
                            return

            pygame.display.update()

    def menu_loop(self):
        self.main_menu()
        is_running = True

        while is_running:
            time_delta = self.clock.tick(60)/1000.0
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    is_running = False

                if event.type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == self.play_button:
                        print("Starting the game")
                        self.start()
                        exit()
                    if event.ui_element == self.options_button:
                        print("options")
                        self.options()
                    if event.ui_element == self.to_menu_button:
                        print("go back to main menu")
                        self.manager.clear_and_reset()
                        self.main_menu()
                    if event.ui_element == self.leaderboard_button:
                        print("showing leaderboard")
                    if event.ui_element == self.credits_button:
                        self.credits()
                    if event.ui_element == self.quit_button:
                        print("Quit the program")
                        is_running = False

                if event.type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED:
                    self.level = event.text
                    print("new level:", self.level)
                    self.options()

                if event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and self.level == "Custom":
                    if event.ui_object_id == "width":
                        width = event.text
                        if str(width).isdigit() and int(width) > 0:
                            print("width", width)
                            self.set_game_width(int(width))
                    if event.ui_object_id == "height":
                        height = event.text
                        if str(height).isdigit() and int(height) > 0:
                            print("height", height)
                            self.set_game_height(int(height))

                self.manager.process_events(event)

                self.manager.update(time_delta)
                self.window_surface.blit(self.background, (0, 0))
                self.manager.draw_ui(self.window_surface)

                pygame.display.update()
