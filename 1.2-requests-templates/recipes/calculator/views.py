from django.shortcuts import render
from django.http import HttpResponseNotFound
from django.urls import reverse

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
    'greek-salad': {
        'огурец, шт': 2,
        'томаты черри, шт': 10,
        'перец болгарский, шт': 1,
        'салат фриллис, уп': 0.5,
        'лук красный, шт': 0.5,
        'фета, уп 250 гр': 0.5,
        'оливки, шт': 10,
        'смесь семян, гр': 10,
        'укроп, гр': 15,
        'петрушка, гр': 15,
        'соль, чл': 0.5,
        'перец черный молотый, чл': 0.5,
        'орегано сушеный, чл': 0.5,
        'масло оливковое нераф., ст. л.': 2,
        'масло подсолнечное нераф., ст. л.': 1,
        'масло кунжутное, чл': 1,
        'соевый соус, ст. л.': 1.5,
        'бальзамический соус (крем), ст. л.': 1,
        'горчица зернистая, ст. л.': 1
    }
    # можете добавить свои рецепты ;)
}


def home(request):
    template = "calculator/menu.html"
    context = {
        'title': 'Рецепты:',
        'heading': 'Доступные рецепты:',
        'empty': 'Нет рецептов',
        'recipes': {k: reverse('details', args=[k]) for k in DATA.keys()}}

    return render(request, template, context)


def recipe_details(request, recipe):
    DEFAULT_SERVINGS = 1
    DIGITS = 2

    template = 'calculator/index.html'
    context = {'recipe': {}}

    try:
        recipe = DATA[recipe]
    except KeyError:
        return HttpResponseNotFound('Рецепт отстутвует')

    servings = request.GET.get('servings', "")
    servings = int(servings) if servings.isdigit() else DEFAULT_SERVINGS
    servings = servings if servings >= 1 else DEFAULT_SERVINGS

    context['recipe'] = {k: round(v * servings, DIGITS)
                         for k, v in recipe.items()}

    return render(request, template, context)
