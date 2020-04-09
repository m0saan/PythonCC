
class RocketSettings():
    """Create the setting of the rocket game. """

    def __init__(self):
        self.width = 600
        self.height = 600
        self.bg_color = (230, 230, 230)
        self.ship_speed_factor = 10

        # Bullet settings
        self.bullet_speed_factor = 10
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullets_allowed = 3
        self.bullet_color = (60, 60, 60)
