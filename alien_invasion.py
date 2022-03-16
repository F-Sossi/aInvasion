import sys
import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:

    def __init__(self):
        pygame.init
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)

        # Set background color
        # self.bg_color = (230,230,230) -> moved to settings

    def run_game(self):
        while True:
            # watch for keyboard events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()

            pygame.display.flip()

if __name__ == '__main__':
    # make game instance and run the game
    ai = AlienInvasion()
    ai.run_game()

