from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def register(request):
    """Sign up user."""
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            authenticated_user = authenticate(username=new_user.username, password=request.POST['password1'])
            # Login user with the username/pw
            login(request, authenticated_user)
            # Redirect to home page
            return HttpResponseRedirect(reverse('blogs:index'))

    context = {'form': form}
    return render(request, 'users/register.html', context)
