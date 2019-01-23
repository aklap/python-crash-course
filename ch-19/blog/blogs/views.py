from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import BlogPost
from .forms import BlogPostForm

# Create your views here.
def index(request):
    """The home page for our Blog website showing all posts."""
    posts = BlogPost.objects.order_by('-date_added')
    context = {'posts': posts}
    return render(request, 'blogs/index.html', context)


def blogpost(request, blogpost_id):
    """View a single post."""
    post = BlogPost.objects.get(id=blogpost_id)
    context = {'post': post}
    return render(request, 'blogs/blogpost.html', context)


def new_blogpost(request):
    """Add a new post."""
    if request.method != 'POST':
        form = BlogPostForm()
    else:
        form = BlogPostForm(data=request.POST)

        if form.is_valid():
            form.save()  # save data to database
            return HttpResponseRedirect(reverse('blogs:index'))

    context = {'form': form}
    return render(request, 'blogs/new_blogpost.html', context)


def edit_blogpost(request, blogpost_id):
    """Edit a post."""
    blogpost = BlogPost.objects.get(id=blogpost_id)

    if request.method != 'POST':
        form = BlogPostForm(instance=blogpost)
    else:
        form = BlogPostForm(instance=blogpost, data=request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('blogs:blogpost', args=[blogpost.id]))
    context = {'blogpost': blogpost, 'form': form}
    return render(request, 'blogs/edit_blogpost.html', context)
