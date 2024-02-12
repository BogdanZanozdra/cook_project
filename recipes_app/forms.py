from django import forms

from .models import Category


class RecipeForm(forms.Form):
    title = forms.CharField(label='Название блюда', max_length=50)
    description = forms.CharField(label='Описание',max_length=200)
    cooking_steps = forms.CharField(label='Шаги приготовления', widget=forms.Textarea)
    image = forms.ImageField(label='Изображение')
    category = forms.ModelChoiceField(label='Выберите категорию', queryset=Category.objects.all())
