from django.urls import path
from . import views

urlpatterns = [
    path('', views.mealplan, name="planner"),
    path('<slug:slug>', views.filter_days, name="filterdays"),
    

    # save meal plan
    path('save-meal/<int:id>/', views.save_plan, name='save_plan')
]
