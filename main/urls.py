from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name="home"),
    # allrecipes
    path('recipes/', views.recipes, name="recipes"),
    path('recipes-details/<int:id>', views.recipe_details, name="recipeDetails"),
    path('recipes/<slug:slug>', views.filter_category, name="filterCategory"),
    path('submit_review/<int:id>', views.submit_review, name='review'),
    # save notes
    path('save_notes/<int:id>', views.save_notes, name='addnotes'),
    path('delete_notes/<int:id>', views.delete_note, name='deletenotes'),
    

]
