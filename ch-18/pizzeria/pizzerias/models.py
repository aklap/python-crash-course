from django.db import models

class Pizza(models.Model):
    """A pizza the pizzeria sells."""
    name = models.CharField(max_length=100)


class Topping(models.Model):
    """A topping for a pizza."""
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
