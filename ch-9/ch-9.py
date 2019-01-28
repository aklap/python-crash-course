"""Ch. 9."""
from restaurant import Restaurant


# 9-1
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

# 9-1 exercises
# restaurant = Restaurant('Kiss\'o', 'Japanese', 12)
# restaurant.describe_restaurant()
# restaurant.open_restaurant()
# print(restaurant.number_served)

# restaurant.set_number_served(432)
# restaurant.increment_number_served()
# print(restaurant.number_served)

# 9-2 exercises
# omen = Restaurant('Omen', 'Japanese')
# cider = Restaurant('Brooklyn Cider House', 'Spanish')
# sams = Restaurant('Sam\'s Caribbean', 'Jamaican')

# omen.describe_restaurant()
# cider.describe_restaurant()
# sams.describe_restaurant()

# 9-3
class User:
    """Base class for User."""

    def __init__(self, name, age, location, login_attempts):
        """Initialize instance of User."""
        self.name = name
        self.age = age
        self.location = location
        self.login_attempts = login_attempts

    def describe_user(self):
        """Print each attribute of the User instance."""
        msg = 'User summary:\n'
        msg += self.name.title()
        msg += ' '
        msg += str(self.age)
        msg += ' '
        msg += self.location.title())
        print(msg)


    def greet_user(self):
        """Greet user."""
        print('Hello, ' + self.name + '!\n')

    def increment_login_attempts(self):
        """Increment login_attempts attribute."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Resets login_attempts to 0."""
        self.login_attempts = 0

# 9-3 exercises
# alexis = User('alexis', 33, 'NY', 1)
# # emmanuel = User('emmanuel', 42, 'Paris')
# # theresa = User('…theresa', 65, 'London')
# # alexis.describe_user()
# # alexis.greet_user()
# alexis.increment_login_attempts()
# alexis.increment_login_attempts()
# alexis.increment_login_attempts()
# print(alexis.login_attempts)
# alexis.reset_login_attempts()
# print(alexis.login_attempts)
# emmanuel.describe_user()
# emmanuel.greet_user()
# theresa.describe_user()
# theresa.greet_user()

# 9-6
class IceCreamStand(Restaurant):
    """Base class for ice cream stands."""

    def __init__(self, *flavors):
        self.flavors = flavors

    def get_flavors(self):
        """Print flavors."""
        for flavor in self.flavors:
            print(flavor)

# 9-6 exercises
# stand = IceCreamStand('choco', 'vanilla', 'green tea')
# stand.get_flavors()

# 9-7
class Admin(User):
    """Base class for Admin."""

    def __init__(self):
        """Initialize instance of Admin."""
        self.privileges = Privileges()


# 9-7 exercises
# me = Admin()
# me.show_privileges()


# 9-8
class Privileges:
    """Base class for privileges."""

    def __init__(self):
        """Initialize instance of Privilege."""
        self.privileges = [
            'can add post',
            'can delete post',
            'can ban user'
        ]

    def show_privileges(self):
        """Show Admin privileges."""
        for privilege in self.privileges:
            print(privilege)

# 9-8 exercises
# me = Admin()
# me.privileges.show_privileges()

# 9-9
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
        super().__init__(make, model, year)

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

# 9-9 exercises
# car = ElectricCar('S', 'Tesla', 2016)
# car.get_range()
# car.battery.upgrade_battery()
# car.get_range()

