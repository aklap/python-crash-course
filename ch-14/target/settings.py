class Settings():
    """A class to store all settings for the game."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings.
        self.screen_width = 1200  # in px
        self.screen_height = 800  # in px
        self.bg_color = (230, 230, 230)  # NOTE: Set bg color with tuple of values, RGB.
        # Ship settings
        self.ship_speed_factor = 15  # Move the ship by 1.5 px
        # Bullet settings
        self.bullet_speed_factor = 30
        self.bullet_width = 15
        self.bullet_height = 3
        self.target_width = 30
        self.target_height = 30
        self.bullet_color = (60, 60, 60)  # Dark gray
        self.bullets_allowed = 3
        self.target_speed_factor = 5
        # Limit the number of ships (lives)
        self.target_limit = 3
