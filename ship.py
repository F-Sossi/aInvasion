from email.mime import image
import pygame

class Ship:
    """Class to manage ships"""
    def __init__(self, ai_game) -> None:
        """Set up ship """
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        # start each ship at bottom center
        self.rect.midbottom = self.screen_rect.midbottom

        #Store decimal value for ships horizontal position
        self.x = float(self.rect.x)

        # Movement Flag
        self.moving_right = False
        self.moving_left = False
    
    def update(self):
        """Update the ships positions"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Update rect object from self.x
        self.rect.x = self.x

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)