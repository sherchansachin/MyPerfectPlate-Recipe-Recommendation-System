from django.contrib.auth.models import User
from django.db import models
from main.models import Recipes

# Create your models here.

class DaysName(models.Model):
    days = models.CharField(max_length=100, null=False, blank=False)
    slug = models.SlugField(max_length=50)
    
    def __str__(self):
        return self.days

        

class MealPlan(models.Model):
    day = models.ForeignKey(DaysName, on_delete=models.SET_NULL, null=True, related_name='plandays')
    recipe = models.ForeignKey(Recipes, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return '{} added a {} plan for {}'.format(self.user, self.recipe.title, self.day)

