"""A class to represent game statistics."""
class Stats():
    """Hold state about a game instances stats."""
    def __init__(self, ai_settings):
        """Initialize stats"""
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = False

    def reset_stats(self):
        """Initialize the stats that can change during the game."""
        self.ships_left = self.ai_settings.ship_limit
