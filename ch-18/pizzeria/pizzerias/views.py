from django.shortcuts import render
from .models import Pizza

# Create your views here.
def index(request):
    """The home page for our Pizzeria website."""
    return render(request, 'pizzerias/index.html')
