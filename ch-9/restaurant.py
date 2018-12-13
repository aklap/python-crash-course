class Restaurant:
    """Base class for restaurants."""

    def __init__(self, restaurant_name, cuisine_type, number_served=0):
        """Initialize an instance of Restaurant."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served

    def describe_restaurant(self):
        """Print the name and cuisine of a Restaurant instance."""
        print(self.restaurant_name)
        print(self.cuisine_type)

    def open_restaurant(self):
        """Print that the restaurant is open."""
        print(self.restaurant_name + " is open!")

    def set_number_served(self, n):
        """Change number_served of a Restaurant instance."""
        self.number_served = n

    def increment_number_served(self):
        """Increment number_served attribute by 1."""
        self.number_served += 10
