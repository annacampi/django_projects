from django.shortcuts import render
from .models import Recipe
from django.template import loader
from django.http import HttpResponse

def recipes(request):
    my_recipes = Recipe.objects.all()
    context = {
        'my_recipes': my_recipes,
    }
    return render(request, 'all_recipies.html', context)

def details(request, id):
    my_recipe = Recipe.objects.get(id=id)
    template = loader.get_template('recipes_details.html')
    context = {
        'my_recipe': my_recipe,
    }
    return HttpResponse(template.render(context, request))

def main(request):
    latest_recipes = Recipe.objects.order_by('-id')[:3]  # Get the last three recipes
    context = {'latest_recipes': latest_recipes}
    return render(request, 'main.html', context)