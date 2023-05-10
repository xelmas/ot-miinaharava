import os
import pygame

dirname = os.path.dirname(__file__)


class Unrevealed(pygame.sprite.Sprite):
    """Represents an unrevealed tile in the Minesweeper game."""

    def __init__(self, x_cor, y_cor):
        """Initializes a new Unrevealed tile with given coordinates.

        Args:
            x_cor (int): The x-coordinate of the given tile.
            y_cor (int): The y-coordinate of the given tile.
        """
        super().__init__()
        self.image = pygame.image.load(
            os.path.join(dirname, "..", "assets/images", "zero.png")
        )
        self.rect = self.image.get_rect()
        self.rect.x = x_cor
        self.rect.y = y_cor
