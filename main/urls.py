from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name="home"),
    # allrecipes
    path('recipes/', views.recipes, name="recipes"),
    path('recipes-details/<int:id>', views.recipe_details, name="recipeDetails"),
    path('recipes/<slug:slug>', views.filter_category, name="filterCategory"),
]
