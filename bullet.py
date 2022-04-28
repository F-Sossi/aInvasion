import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Class for managing bullet functions"""
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = ai_game.settings.bullet_color

        # set up bullet and place on center of the ship
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # store bullet position
        self.y = float(self.rect.y)
    
    def update(self):
        """Move the bullet up the screen from the ships position when fired"""
        # update position of bullet at rate defined in settings.py
        self.y -= self.settings.bullet_speed
        # Update rect position
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw bullet"""
        pygame.draw.rect(self.screen, self.color, self.rect)
