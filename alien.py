from pickle import FALSE, TRUE
from typing import Literal
import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent alien invader craft"""

    def __init__(self, ai_game) -> None:
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # load image and set rect attribute
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Start each new alien at the top left of screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store horizontal position of the alien
        self.x = float(self.rect.x)
        
    def update(self):
        """Move aliens to the right"""
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x

    def check_edges(self) -> bool:
        """Return true if alien hit the edge of the screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True


