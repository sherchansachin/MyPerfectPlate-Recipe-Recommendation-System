from django.urls import path

from accounts.forms import PwdResetForm, PwdResetConfirmForm
from . import views
from django.contrib.auth import views as auth_views

import accounts


urlpatterns = [ 
    path('login_user/', views.loginUser , name='login'),
    path('logout/', views.logoutUser , name='logout'),
    path('register/', views.register, name='register'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='accounts/pwd_reset_form.html', form_class=PwdResetForm), name = 'password_reset'),
    
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='accounts/pwd_reset_done.html'), name = 'password_reset_done'),

    path('password_reset_confirm/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html', form_class=PwdResetConfirmForm), name="password_reset_confirm"),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'), name = 'password_reset_complete'),
    

]