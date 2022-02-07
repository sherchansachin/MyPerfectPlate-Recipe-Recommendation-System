from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from . import forms
from main.models import Recipes

from .forms import RegistrationForm, UserDetailForm
# Create your views here.


# save recipes
@login_required
def save_recipe(request, id):
    recipe = get_object_or_404(Recipes, id=id)
    if recipe.favourites.filter(id=request.user.id).exists():
        recipe.favourites.remove(request.user)
    else:
        recipe.favourites.add(request.user)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def saved_list(request):
    saved_list = Recipes.objects.filter(favourites=request.user)
    return render(request, 'accounts/saves.html', {'saved_list': saved_list})


@login_required
def profile(request):
    return render(request, 'accounts/profile.html')


@login_required
def edit_user(request):
    
    if request.method == 'POST':
        edit_form = UserDetailForm(instance=request.user, data=request.POST)
        if edit_form.is_valid():
            # check & save the user's changed details
            edit_form.save()
    else:
        edit_form = UserDetailForm(instance=request.user)
    return render(request, 'accounts/edit_detail.html', {'edit_form': edit_form})



def register(request):

    if request.user.is_authenticated:
        return redirect("home")

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # authenticate and login
            login(request, user)
            # messages.success(request, "Registered successfully! ")
            return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, 'accounts/register.html', {'form':form})




def loginUser(request):

    if request.user.is_authenticated:
        return redirect("home")


    if request.method == 'POST':
        form = forms.UserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request,username=username, password=password)

            if user is not None:
                login(request, user)
                # messages.success(request, "Logged in successfully! ")
                return redirect("home")
        else:
            # messages.error(request, 'Invalid username or password, Note that both fields may be case-sensitive.')
            return render(request, 'accounts/login.html', context={'form':form})

    else:
        form = forms.UserLoginForm()
        return render(request, 'accounts/login.html', context={'form':form})


    

# logout
def logoutUser(request):
    logout(request)
    messages.success(request, ("You were successfully logged out"))
    return redirect('login')