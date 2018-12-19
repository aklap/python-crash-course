import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    def setUp(self):
        """Create an employee and set up attributes."""
        self.employee = Employee('Alexis', 'LP', 75000)

    def test_give_default_raise(self):
        """Test that there's a default increase for salary."""
        self.employee.give_raise()
        self.assertEqual(self.employee.annual_salary, 80000)

    def test_give_custom_raise(self):
        """Test that we can give a custom raise to an employee."""
        self.employee.give_raise(10000)
        self.assertEqual(self.employee.annual_salary, 85000)

unittest.main()