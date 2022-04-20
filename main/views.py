from django.shortcuts import render, get_object_or_404, redirect
from datetime import datetime
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib.auth.decorators import login_required
from .models import Category, Recipes, Rating
from .forms import ReviewForm
from django.contrib import messages
import pandas as pd
import joblib


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

#recommendation function

# def recommendation(recipe_name):
#     filename = 'model_pickle.pkl'
#     mdl = joblib.load(filename) 
#     df = pd.read_csv("complete.csv")
#     df = df.set_index("title")
#     distances, indices = mdl.kneighbors(df.loc[recipe_name,:].values.reshape(1, -1), n_neighbors = 6)
#     ind = indices.flatten()
#     dist = distances.flatten()
#     recommendated_book = []
#     for i in range(0, len(distances.flatten())):
#         if i == 0:
#             pass
#         else:
#             recommendated_book.append(df.index[ind[i]])
#     return recommendated_book


def recipe_details(request, id):
    '''
    this function based view shows the detail information of a particular recipe
    '''
    details = get_object_or_404(Recipes, pk=id)

    # recipe_name = details.title
    # obj_list = []
    # print(recipe_name)
    # try:
    #     recipes = recommendation(recipe_name)
    #     print(recipes)
    #     for i in recipes:
    #         obj = Recipes.objects.get(title = i)
    #         obj_list.append(obj)

    # except:
    #     print("something went wrong")

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
                                                'reviews': reviews
                                                # 'recommendated':obj_list
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


