from django.test import TestCase
from django.urls import reverse
from .models import Recipe, Category

class RecipeViewsTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Створення тестових даних
        cls.category = Category.objects.create(name='Test Category')
        for i in range(20):
            Recipe.objects.create(
                title=f'Recipe {i}',
                description='Test description',
                instructions='Test instructions',
                ingredients='Test ingredients',
                category=cls.category
            )

    def test_main_view(self):
        response = self.client.get(reverse('main'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipe/main.html')
        self.assertIn('recipes', response.context)
        self.assertEqual(len(response.context['recipes']), 10)