from django.contrib import admin
from .models import Recipes, Category, Rating, Notes
# Register your models here.
admin.site.register(Recipes)
admin.site.register(Category)
admin.site.register(Rating)
admin.site.register(Notes)
