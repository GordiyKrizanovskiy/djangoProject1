from django.shortcuts import render
from .models import Recipe, Category

def main(request):
    recipes = Recipe.objects.order_by('?')[:10]
    return render(request, 'recipe/main.html', {'recipes': recipes})

def category_detail(request):
    categories = Category.objects.all()
    return render(request, 'recipe/category_detail.html', {'categories': categories})