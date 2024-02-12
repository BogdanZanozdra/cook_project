import random

from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, get_object_or_404
from .models import Recipe
from .forms import RecipeForm


def index(request):
    recipes = Recipe.objects.all()
    random_recipes = []
    for i in range(5):
        random_recipes.append(random.choice(recipes))
    return render(request, 'recipes_app/index.html', {'random_recipes': random_recipes})


def full_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    return render(request, 'recipes_app/full_recipe.html', {'recipe': recipe})


def new_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        message = 'Ошибка данных'
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            cooking_steps = form.cleaned_data['cooking_steps']
            image = form.cleaned_data['image']
            fs = FileSystemStorage()
            fs.save(image.name, image)
            category = form.cleaned_data['category']
            author = request.user
            recipe = Recipe(title=title, description=description, cooking_steps=cooking_steps,
                            image=image, category=category, author=author)
            recipe.save()
            message = 'Рецепт сохранен'
    else:
        form = RecipeForm()
        message = 'Заполните форму создания рецепта'
    return render(request, 'recipes_app/new_recipe.html', {'form': form, 'message': message})


def update_recipe(request, recipe_id):
    message = 'Ошибка данных'
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = Recipe.objects.get(pk=recipe_id)
            form = RecipeForm(request.POST, instanse=recipe)
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            cooking_steps = form.cleaned_data['cooking_steps']
            image = form.cleaned_data['image']
            fs = FileSystemStorage()
            fs.save(image.name, image)
            category = form.cleaned_data['category']
            author = form.cleaned_data['author']
            recipe = Recipe(title=title, description=description, cooking_steps=cooking_steps,
                            image=image, category=category, author=author)
            recipe.save()
            message = 'Рецепт изменен'
    else:
        form = RecipeForm()
        message = 'Заполните форму создания рецепта'
    return render(request, 'recipes_app/new_recipe.html', {'form': form, 'message': message})







