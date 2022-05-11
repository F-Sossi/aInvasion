import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent alien invader craft"""

    def __init__(self, ai_game) -> None:
        super().__init__()
        self.screen = ai_game.screen

        # load image and set rect attribute
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Start each new alien at the top left of screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store horizontal position of the alien
        self.x = float(self.rect.x)


