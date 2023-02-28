from django_filters import FilterSet, CharFilter, MultipleChoiceFilter
from .models import Recipe


class RecipeFilter(FilterSet):
    name_recipe = CharFilter(field_name='name_recipe', lookup_expr='icontains')
    cuisine = CharFilter(field_name='cuisine', lookup_expr='exact')
    # meal_type =

    class Meta:
        model = Recipe
        fields = [
            'name_recipe',
            'cuisine',
        ]

        # http: // 127.0.0.1: 8000 /?category00 = on & category10 = on & category13 = on & cuisine00 = on & cuisine16 = on & cuisine20 = on & ingredient00 = on & ingredient16 = on & ingredient20 = on & search =
