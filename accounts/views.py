from multiprocessing import context
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required

from accounts.models import Profile
from . import forms
from main.models import Recipes

from .forms import RegistrationForm, UserDetailForm, UserUpdateForm, ProfileUpdateForm
# Create your views here.


# save recipes
@login_required
def save_recipe(request, id):
    recipe = get_object_or_404(Recipes, id=id)
    if recipe.favourites.filter(id=request.user.id).exists():
        recipe.favourites.remove(request.user)
    else:
        recipe.favourites.add(request.user)
        messages.success(request, 'Recipe saved successfully!')
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def saved_list(request):
    saved_list = Recipes.objects.filter(favourites=request.user)
    save_count = saved_list.count()
    return render(request, 'accounts/saves.html', {'saved_list': saved_list, 'save_count': save_count})


@login_required
def profile(request):

    if request.method == 'POST':
        # instances of form
        uuser_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES,  instance=request.user.profile)

        if uuser_form.is_valid() and p_form.is_valid():
            uuser_form.save()
            p_form.save()
            messages.success(request, f'Your account information has been updated!')
            # post, get, redirect pattern
            return redirect('profile')
    else:
        
        uuser_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'uuser_form': uuser_form,
        'p_form': p_form
    }
    return render(request, 'accounts/profile.html', context)


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