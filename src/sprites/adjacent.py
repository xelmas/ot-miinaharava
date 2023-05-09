import os
import pygame

dirname = os.path.dirname(__file__)


class Adjacent(pygame.sprite.Sprite):
    def __init__(self, x_cor=0, y_cor=0, value=0):
        super().__init__()
        self.value = value
        self.image = pygame.image.load(
            os.path.join(dirname, "..", "assets/images",
                         str(self.value)+".png")
        )
        self.rect = self.image.get_rect()
        self.rect.x = x_cor
        self.rect.y = y_cor
