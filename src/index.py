import pygame
from minesweeper import Minesweeper

CELL_SIZE = 50

def main():
    height = 5
    width = 8
    num_mines = 6
    
    display_height = height * CELL_SIZE
    display_width = width * CELL_SIZE
    display = pygame.display.set_mode((display_width, display_height))
    pygame.display.set_caption("Minesweeper")
    game = Minesweeper(width, height,num_mines,CELL_SIZE)
    pygame.init()
    game.all_sprites.draw(display)

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.update()

    pygame.quit()
    game.play()


if __name__ == "__main__":
    main()