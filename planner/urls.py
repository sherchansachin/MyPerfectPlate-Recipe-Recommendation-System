from django.urls import path
from . import views

urlpatterns = [
    path('', views.mealplan, name="mealplan"),
]
