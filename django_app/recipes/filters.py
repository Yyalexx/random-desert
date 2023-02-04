from django_filters import FilterSet, CharFilter
from .models import Recipe


class RecipeFilter(FilterSet):
    name_recipe = CharFilter(field_name='name_recipe', lookup_expr='icontains', label='Рецепт')

    class Meta:
        model = Recipe
        fields = [
            'name_recipe',
        ]
