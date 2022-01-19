from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import  UserCreationForm, PasswordResetForm, SetPasswordForm, AuthenticationForm


class UserLoginForm(AuthenticationForm):

    username = forms.CharField(widget=forms.TextInput(
        attrs={ 'id': 'login-username', 'autofocus': 'autofocus' }))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'id': 'password'}))

class RegistrationForm(UserCreationForm):
    #additional field
    email = forms.EmailField(required=True)

    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control mb-3',  'id': 'password'})
    )
    password2 = forms.CharField(
        label='Password Confirmation',
        widget=forms.PasswordInput(attrs={'class': 'form-control mb-3', 'id': 'password2'})
    )

    def clean_email(self):
        if User.objects.filter(email=self.cleaned_data['email']).exists():
            raise forms.ValidationError("The email is already registered, try another email")
        return self.cleaned_data['email']

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']




class PwdResetForm(PasswordResetForm):

    email = forms.EmailField(max_length=254, widget=forms.TextInput(
        attrs={'class': 'form-control mb-3', 'placeholder': 'Email', 'id': 'form-email'}))

# check to see if user email exists or not in the database
    def clean_email(self):
        email = self.cleaned_data['email']
        test = User.objects.filter(email=email)
        if not test:
            raise forms.ValidationError(
                'Unfortunatley we can not find that email address')
        return email


class PwdResetConfirmForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label='New password', widget=forms.PasswordInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'New Password', 'id': 'form-newpass'}))
    new_password2 = forms.CharField(
        label='Repeat password', widget=forms.PasswordInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'New Password', 'id': 'form-new-pass2'}))


# user details edit form
class UserDetailForm(forms.ModelForm):
    
    first_name = forms.CharField(
        label='Firstname', min_length=4, max_length=50, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'Firstname', 'id': 'form-firstname'}))

    last_name = forms.CharField(
        label='Lastname', min_length=4, max_length=50, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'Lastname', 'id': 'form-lastname'}))

    email = forms.EmailField(
        max_length=200, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'Old Password', 'id': 'form-email'}))

    

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

    def clean_email(self):
        email = self.cleaned_data['email']
        # get the logged in users email address
        c_user_email = self.instance.email
        # only filter with the emails of users except the logged in user's email
        if User.objects.filter(email__iexact=email).exclude(email__iexact=c_user_email).count() > 0:
            raise forms.ValidationError(
                'Please use another Email, that is already taken')
        return email

    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['last_name'].required = False
        self.fields['email'].required = False