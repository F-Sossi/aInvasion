class Settings:
    """ A class to store all settings for the game"""

    def __init__(self) -> None:
        # screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)
        # Ship settings
        self.ship_speed = 1.5