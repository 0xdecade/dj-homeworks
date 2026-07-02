from django.shortcuts import render
from django.http import HttpResponse
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
    LINK = '''<a href="{}">{}</a>'''
    links = {k: reverse('details', args=[k]) for k in DATA.keys()}
    msg = "<li>".join(["<ul>"] + [LINK.format(link, title)
                      for title, link in links.items()])
    msg = "<div>Доступные рецепты:</div>" + msg
    return HttpResponse(msg)


def recipe_details(request, recipe):
    context = _select_recipe(recipe)
    servings = request.GET.get('servings', "")
    servings = int(servings) if servings.isdigit() else None

    # Проверим наличие параметра servings
    has_servings = _check_servings(servings)

    # Мы можем отдать результат сразу если параметра нет
    if not has_servings:
        return _render_recipe(request, context)

    # Проверим, что параметр servings это целое положительное целое
    servings_is_valid = _validate_servings(servings)

    # Пересчитаем количество ингридиентов
    if servings_is_valid:
        context['recipe'] = _calc_servings(context, servings)

    return _render_recipe(request, context)


def _select_recipe(recipe) -> dict:
    """ Функция выбора рецепта """
    # Пытаемся выбрать рецепт из словаря
    # Чтобы избежать изменения по ссылке копируем его путем распаковки
    return {'recipe': {**DATA.get(recipe, {})}}


def _check_servings(servings) -> bool:
    """ Функция проверки наличия параметра servings """
    return servings is not None


def _render_recipe(request, context) -> HttpResponse:
    """ Функция рендеринга рецепта """
    return render(request, 'calculator/index.html', context)


def _calc_servings(context, servings) -> dict:
    """ Функция калькулятора порций """
    return {k: round(v * servings, 2) for k, v in context['recipe'].items()}


def _validate_servings(servings) -> bool:
    """ Функция валидации порций """
    return servings > 1

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
