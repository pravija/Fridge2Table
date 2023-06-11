from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import IngredientForm
from .models import Ingredient
from . import ingredients as ing
@login_required(login_url="/login")
def home(request):
    ingredients_list = []
    if request.method == 'POST':
        form = IngredientForm(request.POST)
        if form.is_valid():
            ingredients = form.cleaned_data['ingredients'] 
            ingredients_list = ingredients.split(',')
            Ingredient.objects.create(name='new_list')
            for ingredient in ingredients_list:
                Ingredient.objects.create(name=ingredient.strip())
            ing.score(ingredients)
        #     ingredients = Ingredient.objects.all()
        #     list_index = 0
        #     for i in range(len(ingredients)):
        #       if ingredients[i].name == "new_list":
        #          list_index = i+1
        #     context = {'ingredients': ingredients, 'list_index': list_index}
        # return render(request, 'main/ingredients_added.html', context)
        return render(request,'main/home.html')
    else:
        return render(request,'main/home.html')
     

def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/home')
    else:
        form = RegisterForm()

    return render(request, 'registration/sign_up.html', {"form": form})


def add_ingredients(request):
    if request.method == 'GET':
            ingredients = Ingredient.objects.all()
            list_index = 0
            for i in range(len(ingredients)):
              if ingredients[i].name == "new_list":
                 list_index = i+1
            context = {'ingredients': ingredients, 'list_index': list_index}
    return render(request, 'main/ingredients_added.html', context) 