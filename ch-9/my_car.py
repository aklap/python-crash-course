from car import Car, ElectricCar
# NOTE: Each class in a module should be related somehow.

my_new_car = Car('audi', 'a4', '2016')
print(my_new_car.get_range())

# NOTE: You can use dot notation to avoid naming conflicts, eg car.Car or car.ElectricCar

# NOTE:

# Project folder tree looks like:

# /Project
# |__module.py (All code related to car)
  # |  • Car class
  # |  • ElectricCar
  # |  • Battery
# |
# |__import parent class to instantiate instance of class Car
