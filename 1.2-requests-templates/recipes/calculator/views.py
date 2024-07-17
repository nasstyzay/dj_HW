from django.shortcuts import render
from django.http import HttpResponseNotFound

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}


def recipe_view(request, recipe):
    if recipe not in DATA:
        return HttpResponseNotFound('Рецепт не найден.')

    servings = request.GET.get('servings', 1)
    try:
        servings = int(servings)
        if servings < 1:
            raise ValueError
    except ValueError:
        return HttpResponseNotFound('Количество порций должно быть положительным целым числом.')

    ingredients = DATA[recipe]
    context = {
        'recipe': {ingredient: amount * servings for ingredient, amount in ingredients.items()}
    }
    return render(request, 'calculator/recipe.html', context)
