from django.contrib.auth.models import User
from django.db import models
from autoslug import AutoSlugField


class Category(models.Model):
    main_category = models.TextField(default='')
    slug = AutoSlugField(populate_from='main_category',default='')
    
    def __str__(self):
        return self.main_category


class Recipes(models.Model):

    title = models.TextField(max_length=150)
    preptime = models.TextField(max_length=50)
    tags = models.TextField(default='')
    ingredients = models.TextField(default='')
    instructions = models.TextField(default='')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    image = models.TextField(default='')
    calories = models.TextField(default='')
    carbs = models.TextField(default='')
    sod = models.TextField(default='')
    cho = models.TextField(default='')
    fat = models.TextField(default='')
    pro = models.TextField(default='')
    created_by = models.CharField(max_length=250, default='')
    favourites = models.ManyToManyField(User, related_name='favourites', default=None, blank=True)

    def __str__(self):
        return self.title

