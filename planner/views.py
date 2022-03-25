from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView, ListView
from main.models import Recipes
from django.contrib import messages
from planner.models import DaysName, MealPlan

# Create your views here.

@login_required
def mealplan(request):
    '''
      function to show the meal plans saved to db
    '''

    #get all day list
    days = DaysName.objects.all()

    saved_plans = MealPlan.objects.filter(user=request.user.id )

    recipe_list = []
    

    for saved in saved_plans:
        recipe_list.append(saved.recipe)





    return render(request, 'planner/planner.html', {'recipe_list': recipe_list,
                                                    'saved_plans': saved_plans,
                                                    'days': days})



def filter_days(request, slug):
    '''
    
    '''
    individual_day = get_object_or_404(DaysName, slug=slug)

    saved_plans = MealPlan.objects.filter(day=individual_day, user=request.user.id)
    recipe_list = []

    for saved in saved_plans:
        recipe_list.append(saved.recipe)


    count = saved_plans.count()

    days = DaysName.objects.all()

    return render(request, 'planner/mealplans.html', {'individual_day': individual_day,
                                                    'saved_plans':saved_plans,
                                                    'count': count,
                                                    'recipe_list': recipe_list,
                                                    'days':days})


@login_required
def save_plan(request,id):
    recipe  = get_object_or_404(Recipes, id=id)

    days = DaysName.objects.all()

    day= None
    # get data (days selected) and store to models
    if request.method == 'POST':
        data = request.POST

        # see if duplicate entries
        user_id = request.user.id
        recipe_id = id

        if not MealPlan.objects.filter(user_id=user_id, recipe_id=recipe_id).exists():
            if data['day'] != 'none':
                day = DaysName.objects.get(id=data['day'])
                planned = MealPlan.objects.create(
                    day=day,
                    recipe=recipe,
                    user=request.user
                )
            else:
                print("This meal plan is already for the particular day,")

    print('day:', day)
    


    return render(request, 'planner/addmeal.html', {"recipe":recipe,
                                                    "days": days})
