class Settings():
    """A class representing all game settings. """

    def __init__(self):
        # General Settings.
        self.sc_width = 600
        self.sc_height = 600
        self.bg_color = (230, 230, 230)
        self.bullet_color = (60, 60, 60)

        # Ship setting
        self.move_speed_factor = 2

        # Bullet settings
        self.bullet_width = 2
        self.bullet_hight = 15
        self.bullet_speed = 10

        # Alien settings
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
