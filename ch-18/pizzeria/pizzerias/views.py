from django.shortcuts import render
from .models import Pizza

# Create your views here.
def index(request):
    """The home page for our Pizzeria website."""
    return render(request, 'pizzerias/index.html')

def pizzas(request):
    """List all available pizzas."""
    pizzas = Pizza.objects.order_by('name')
    context = {'pizzas': pizzas}
    return render(request, 'pizzerias/pizzas.html', context)

def pizza(request, pizza_id):
    """Show info about a single kind of pizza."""
    pizza = Pizza.objects.get(id=pizza_id)
    toppings = pizza.topping_set.order_by('name')
    context = {'pizza': pizza, 'toppings': toppings}
    return render(request, 'pizzerias/pizza.html', context)
