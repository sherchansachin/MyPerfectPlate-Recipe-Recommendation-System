from django.shortcuts import render, get_object_or_404
from datetime import datetime
from .models import Category, Recipes
# Create your views here.




def home(request):
  
    return render(request, 'main/home.html')


def recipes(request):
    '''
    this function based view displays all the recipes from db
    '''
    all_recipes = Recipes.objects.all()
    recipe_count = Recipes.objects.count()
    categories = Category.objects.all()

    # get the top 4 recently viewed recipes
    recently_viewed = Recipes.objects.all().order_by('-recently_viewed')[0:4]

    return render(request, "main/recipes.html", {"all_recipes": all_recipes,
                                                "recipe_count": recipe_count,
                                                "categories": categories ,
                                                "recently_viewed"   : recently_viewed
                                                })



def filter_category(request, slug):
    '''
    this function based view filters through the categories of recipes
    '''
    individual_cat = get_object_or_404(Category, slug=slug)
    recipes = Recipes.objects.filter(category=individual_cat)
    count = recipes.count()
    return render(request, 'main/category.html', {'individual_cat': individual_cat,
                                                    'recipes':recipes,
                                                    'count': count})



def recipe_details(request, id):
    '''
    this function based view shows the detail information of a particular recipe
    '''
    details = get_object_or_404(Recipes, pk=id)

    # capture the dateandtime for recently viewed recipes
    details.recently_viewed = datetime.now()
    details.save()

    # check if the particular recipe is saved by a user or not
    fav = bool

    if details.favourites.filter(id=request.user.id).exists():
        fav = True
        
    tags = details.tags.split('#')
    ingredients = details.ingredients.split('#')
    instructions = details.instructions.split('#')
    categories = details.tags.split("#")
    return render(request, 'main/recipe_details.html', {'details': details, 
                                                'ingredients': ingredients,
                                                'instructions': instructions,
                                                'categories': categories,
                                                'tags': tags,
                                                'fav': fav,
                                                })
    