from django.urls import path
from .views import index, full_recipe, new_recipe, update_recipe

app_name = 'recipes_app'

urlpatterns = [
    path('', index, name='index'),
    path('full_recipe/<int:recipe_id>/', full_recipe, name='full_recipe'),
    path('new_recipe', new_recipe, name='new_recipe'),
    path('update_recipe/<int:recipe_id>/', update_recipe, name='update_recipe'),

]