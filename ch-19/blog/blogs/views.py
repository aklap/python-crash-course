from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from .models import BlogPost
from .forms import BlogPostForm

# Create your views here.
def index(request):
    """The home page for our Blog website showing all posts."""
    posts = BlogPost.objects.filter(author=request.user).order_by('-date_added')
    context = {'posts': posts}
    return render(request, 'blogs/index.html', context)

@login_required
def blogpost(request, blogpost_id):
    """View a single post."""
    post = BlogPost.objects.get(id=blogpost_id)
    if post.author != request.user:
        Http404

    context = {'post': post}
    return render(request, 'blogs/blogpost.html', context)

@login_required
def new_blogpost(request):
    """Add a new post."""
    if request.method != 'POST':
        form = BlogPostForm()
    else:
        form = BlogPostForm(data=request.POST)

        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.author = request.user
            new_topic.save()
            form.save()  # save data to database
            return HttpResponseRedirect(reverse('blogs:index'))

    context = {'form': form}
    return render(request, 'blogs/new_blogpost.html', context)

@login_required 
def edit_blogpost(request, blogpost_id):
    """Edit a post."""
    blogpost = BlogPost.objects.get(id=blogpost_id)

    if blogpost.author != request.user:
        raise Http404

    if request.method != 'POST':
        form = BlogPostForm(instance=blogpost)
    else:
        form = BlogPostForm(instance=blogpost, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blogs:blogpost', args=[blogpost.id]))

    context = {'blogpost': blogpost, 'form': form}
    return render(request, 'blogs/edit_blogpost.html', context)
