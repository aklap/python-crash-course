class Stats():
    """Keep track of stats in a game."""
    def __init__(self, settings):
        """Initialize ball instance."""
        self.settings = settings
        self.reset_stats()
        self.game_active = True

    def reset_stats(self):
        """Initialize the stats that can change."""
        self.balls_left = self.settings.ball_limit