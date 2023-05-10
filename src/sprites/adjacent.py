import os
import pygame

dirname = os.path.dirname(__file__)


class Adjacent(pygame.sprite.Sprite):
    """Represents an adjacent tile in the Minesweeper game."""

    def __init__(self, x_cor, y_cor, value=0):
        """Initializes a new Adjacent tile with given coordinates and value.

        Args:
            x_cor (int): The x-coordinate of the given tile.
            y_cor (int): The y-coordinate of the given tile.
            value (int): The value of adjacent mines. Defaults to 0.
        """
        super().__init__()
        self.value = value
        self.image = pygame.image.load(
            os.path.join(dirname, "..", "assets/images",
                         str(self.value)+".png")
        )
        self.rect = self.image.get_rect()
        self.rect.x = x_cor
        self.rect.y = y_cor
