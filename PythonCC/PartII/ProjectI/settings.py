"""A module that contains a class of game settings"""


class Settings():
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""

        # Screen settings
        self.screen_width = 600
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        self.ship_speed_factor = 1.5

        # Ship settings
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed_factor = 10
        self.bullet_width = 2
        self.bullet_height = 15
        self.bullets_allowed = 3
        self.bullet_color = (60, 60, 60)

        # Alien settings
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 40
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
