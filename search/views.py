from django.db.models import Q
from django.shortcuts import render
from main.models import Recipes
from django.http import HttpResponseRedirect
# Create your views here.


def search(request):
    '''
    function based view to search recipes by recipe ingredients name and category
    '''
    if request.method == 'GET':
        query = request.GET.get('q')
        # print(query)
        if query:
            for ing in query.split():
                recipes = Recipes.objects.filter(Q(ingredients__icontains=ing ) | Q(tags__icontains=ing))
                count_search = recipes.count()
                print(ing)
            return render(request, 'main/searched.html', {'recipes': recipes, 'count_search': count_search, 'query': query})
        else:
            print('No recipes found')
            return render(request, 'main/searched.html', {})