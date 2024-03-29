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
    calories = models.CharField(max_length=10, default='')
    carbs = models.CharField(max_length=10, default='')
    sod = models.CharField(max_length=10, default='')
    cho = models.CharField(max_length=10, default='')
    fat = models.CharField(max_length=10, default='')
    pro = models.CharField(max_length=10, default='')
    created_by = models.CharField(max_length=250, default='')
    favourites = models.ManyToManyField(User, related_name='favourites', default=None, blank=True)
    recently_viewed = models.DateTimeField(blank=True, null=True)
    num_visits = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title

class Rating(models.Model):
    recipe = models.ForeignKey(Recipes, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.CharField(max_length=500, blank=True)
    ratings = models.FloatField()
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return '{} rated {} plan for {}'.format(self.user, self.ratings, self.recipe)

class Note(models.Model):
    recipe = models.ForeignKey(Recipes, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    note = models.TextField(max_length=400)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} saved a note for {}'. format(self.user, self.recipe)