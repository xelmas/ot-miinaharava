import pygame
import os

dirname = os.path.dirname(__file__)

class Number(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0, value=0):
        super().__init__()
        self.value = value
        self.image = pygame.image.load(
            os.path.join(dirname, "..", "assets", str(self.value)+".png")
        )
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y