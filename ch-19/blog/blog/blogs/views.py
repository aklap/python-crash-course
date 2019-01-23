from django.shortcuts import render
from .models import BlogPost

# Create your views here.
def index(request):
    """Our homepage for the blog, listing all posts."""
    blogs = BlogPost.objects.order_by('date_added')
    context = {'blogs': blogs}
    return render(request, 'blogs/index.html', context)