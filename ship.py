from email.mime import image
import pygame

class Ship:
    """Class to manage ships"""
    def __init__(self, ai_game) -> None:
        """Set up ship """
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        # start each ship at bottom center
        self.rect.midbottom = self.screen_rect.midbottom

        # Movement Flag
        self.moving_right = False
        self.moving_left = False
    
    def update(self):
        """Update the ships positions"""
        if self.moving_right:
            self.rect.x += 1
        if self.moving_left:
            self.rect.x -= 1

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)