import csv  # https://docs.python.org/3/library/csv.html

# https://django-extensions.readthedocs.io/en/latest/runscript.html

# python3 manage.py runscript recipe_load

from main.models import Category, Recipes

def run():
    fhand = open('main/recipe01.csv')
    reader = csv.reader(fhand)
    next(reader)  # Advance past the header

    Category.objects.all().delete()
    Recipes.objects.all().delete()

    #title, prep, category, ingredient, instruction, pic, recipeby, calo, carbo, sod, cholestrol, fat, protiens, Main_Category

    for row in reader:
        print(row)

        # create for category and recipes

        c, created = Category.objects.get_or_create(main_category=row[13])

        r = Recipes(title=row[0], preptime=row[1], tags=row[2], ingredients=row[3], instructions=row[4], category=c, image=row[5], calories=row[7], carbs=row[8], sod=row[9], cho=row[10], fat=row[11], pro=row[12], created_by=row[6])
        r.save()