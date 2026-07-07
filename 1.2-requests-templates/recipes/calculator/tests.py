from django.test import SimpleTestCase
from django.urls import reverse
from http import HTTPStatus


class RecipeDetailsTest(SimpleTestCase):
    """Тестирование отображения рецепта"""

    def __init__(self, methodName="runTest"):
        super().__init__(methodName)
        self.VIEW = 'details'
        self.KNOWN_RECIPE_URL = reverse(self.VIEW, args=['omlet'])

    def get_url(self, url, data=None):
        print(f" -> Testing URL: {url}" +
              (f" with params {data}" if data else ""))
        return self.client.get(url, data=data)

    def test_unknown(self):
        """Проверка 404 для несуществующего рецепта"""
        url = reverse(self.VIEW, args=['abracadabra'])
        response = self.get_url(url)
        self.assertEqual(response.status_code, HTTPStatus.NOT_FOUND)

    def test_without_param(self):
        """Проверка доступности рецепта без параметров"""
        response = self.get_url(self.KNOWN_RECIPE_URL)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_servings_non_number(self):
        """Проверка передачи строки в значение порции"""
        response = self.get_url(self.KNOWN_RECIPE_URL,
                                data={'servings': 'adsf'})
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_servings_empty_str(self):
        """Проверка передачи пустой строки в значение порций"""
        response = self.get_url(self.KNOWN_RECIPE_URL, data={'servings': ''})
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_servings_float(self):
        """Проверка передачи дробного количества порций"""
        response = self.get_url(self.KNOWN_RECIPE_URL, data={'servings': 1.5})
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_servings_negative(self):
        """Проверка передачи отрицательного количества порций"""
        response = self.get_url(self.KNOWN_RECIPE_URL, data={'servings': -1})
        self.assertEqual(response.status_code, HTTPStatus.OK)
