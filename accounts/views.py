from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages, auth
from django.contrib.auth.forms import AuthenticationForm
from . import forms

from .forms import RegistrationForm
# Create your views here.

def register(request):

    # if request.user.is_authenticated:
    #     return redirect('/')

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']

            # authenticate and login
            user = authenticate(username=email, password=password)
            login(request, user)
            # messages.success(request, "Registered successfully! ")
            return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, 'accounts/register.html', {'form':form})




def loginUser(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
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