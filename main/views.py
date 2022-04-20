from django.shortcuts import render, get_object_or_404, redirect
from datetime import datetime
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib.auth.decorators import login_required
from .models import Category, Recipes, Rating
from .forms import ReviewForm
from django.contrib import messages
import requests
import json




from django.http import HttpResponseRedirect
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

    # paginator
    paginator = Paginator(all_recipes, 20)
    page_num = request.GET.get('page', 1)

    try:
        all_recipes = paginator.page(page_num)

    except PageNotAnInteger:
        all_recipes = paginator.page(1)
        
    except EmptyPage:
        all_recipes = paginator.page(paginator.num_pages)

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

    the function also sends POST request (recipe title) to Flask API where content based
    filtering on the basis of TF-IDF and calculation of cosine-similarity is done.

    Then, the recommendated similar recipes are GET in form of dictonary, where values (recipe name)
    is filtered against the Database and results are passed to templates as context variable.
    '''
    details = get_object_or_404(Recipes, pk=id)

    headers = {
        'content-type': "multipart/form-data",
        'cache-control': "no-cache",
    }

    recommend = None
    obj_list = []
    recipe_name = details.title
    print(recipe_name)
    if recipe_name:
        url = "http://127.0.0.1:5000/get_recommendation"
        payload = {'recipe_name':recipe_name}
        responses = requests.request("POST",url,data=payload)
        print(responses) #got 200 response, OK

        response = json.loads(responses.text)
    
        print(response) # got the response from flask api

        value = tuple(response.values()) #store the values to tuple,
        print(value) # print the individual recipe's values got from flask

        for x in value:
            try:
                '''
                    filtering the recipes database by recipe title, with respect to
                    the obtained flask recommendation api. 
                '''
                recommend = Recipes.objects.get(title=x)
                obj_list.append(recommend) # append to a empty list
            except:
                pass

    # capture the dateandtime for recently viewed recipes
    details.recently_viewed = datetime.now()
    details.save()

    # check if the particular recipe is saved by a user or not
    fav = bool

    if details.favourites.filter(id=request.user.id).exists():
        fav = True
    
     # Get the reviews
    reviews = Rating.objects.filter(recipe_id=id)
        
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
                                                'reviews': reviews,
                                                'recommendated': obj_list
                                                })
    


def submit_review(request, id):
    """
    this function saves a review and rating for a particular recipe
    """
    recipe = get_object_or_404(Recipes, pk=id)

    if request.method == "POST":
        # see if duplicate entries
        user_id = request.user.id
        recipe_id = id

        if not Rating.objects.filter(user_id=user_id, recipe_id= recipe_id).exists():
            review = request.POST['review']
            rate = request.POST['rating']
            ratingObj = Rating()
            ratingObj.recipe = recipe
            ratingObj.user = request.user
            ratingObj.review = review
            ratingObj.ratings = rate
            ratingObj.save()
        else:
            print("ratings and review for this recipe was already givenn")

        return redirect(request.META['HTTP_REFERER'])
    
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


