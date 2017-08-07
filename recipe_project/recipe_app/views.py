from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Recipes


def index(request):
    recipes = Recipes.objects.all()[:25]
    data = {
        'recipes': recipes
    }
    return render(request, 'index.html', context=data)


def details(request, id):
    recipe = Recipes.objects.get(id=id)
    data = {
        'recipe': recipe
    }
    return render(request, 'details.html', context=data)

def create(request):
    print(request)
    if request.method == 'POST':
        title = request.POST['title']
        prep = request.POST['prep_time']
        cook_time = request.POST['cooking_time']
        serving = request.POST['servings']
        photo = request.FILES['photo']
        ingredients = request.POST['ingredients']
        cook_instr = request.POST['cooking_instructions']

        recipe = Recipes(title=title, prep_time=prep, cooking_time=cook_time, servings=serving,
                         photo=photo, cooking_instructions=cook_instr, ingredients=ingredients)
        recipe.save()
        return redirect('/recipes')
    else:
        return render(request, 'create_recipe.html')
