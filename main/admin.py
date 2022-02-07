from django.contrib import admin
from .models import Recipes, Category
# Register your models here.
admin.site.register(Recipes)
admin.site.register(Category)