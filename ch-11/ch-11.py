"""Chapter 11."""


class Employee:
    def __init__(self, first_name, last_name, annual_salary):
        """Initialize an Employee instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, amount=5000):
        """Add $5000 to the annual salary by default."""
        self.annual_salary += amount

    # Use setUp()
    def setUp(self):
        """Create an instance of Employee for use in all test methods."""

    def test_give_default_raise():
        """Test that calling give_raise method without an arg increases the annual_salary attribute by 5000."""

    # test_give_custom_raise()
