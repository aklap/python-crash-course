from car import Car, ElectricCar


my_new_car = Car('audi', 'a4', '2016')
print(my_new_car.get_range())

# NOTE: Use dot notation to avoid naming conflicts, eg car.Car or car.ElectricCar

"""
NOTE: Project folder tree looks like:
    / Project
        |__module.py (All code related to car)
        |  • Car class
        |  • ElectricCar class
        |  • Battery class
        |
        |__import parent class to instantiate instance of class Car
"""
