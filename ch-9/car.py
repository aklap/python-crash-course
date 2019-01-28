"""A module to create instances of class Car, to represent a car."""


class Car():
    """Base Car class."""
    def __init__(self, make, model, year):
        """Initialize instance of class Car."""
        self.make = make
        self.model = model
        self.year = year


class ElectricCar(Car):
    """Child class of parent class Car."""
    def __init__(self, make, model, year):
        """Initialize instance of class ElectricCar."""
        super().__init__(make, model, year)  # Pass args back up to parent init

        self.battery = Battery()

    def get_range(self):
        """Print the range of the instance."""
        if self.battery.battery_size == 70:
            range = 240
        elif self.battery.battery_size == 85:
            range = 250

        msg = 'This car can go approx. ' + str(range)
        print(msg)


class Battery():
    """Base class Battery."""

    def __init__(self, battery_size=70):
        """Initialize instance of Battery."""

        self.battery_size = battery_size

    def describe_battery(self):
        """Print battery size attribute."""
        print(str(self.battery_size) + '-kwH battery')

    def upgrade_battery(self):
        """Check battery size and set capacity to 85."""
        if self.battery_size < 85:
            self.battery_size = 85

        print('Battery capacity upgraded to 85 kwH.')
