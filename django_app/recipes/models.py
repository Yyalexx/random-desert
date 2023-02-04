from django.db import models
from django.core.validators import MinValueValidator


class Recipe(models.Model):
    id_recipe = models.AutoField(primary_key=True)
    name_recipe = models.CharField(max_length=200)
    text_recipe = models.TextField()
    vegeterian = models.BooleanField(default=0)
    calories = models.FloatField(validators=[MinValueValidator(0.0, 'Калорий должно быть >= 0')])
    protein = models.FloatField(validators=[MinValueValidator(0.0, 'Белка должно быть >= 0')])
    fat = models.FloatField(validators=[MinValueValidator(0.0, 'Жиров должно быть >= 0')])
    carbo = models.FloatField(validators=[MinValueValidator(0.0, 'Углеводов должно быть >= 0')])
    portions = models.IntegerField(validators=[MinValueValidator(0, 'Порций должно быть больше ноля')])

    def __str__(self):
        return f'{self.name_recipe}'

    def get_absolute_url(self):
        return f'/recipe/{self.id_recipe}'


class Ingredient(models.Model):
    id_ingr = models.AutoField(primary_key=True)
    name_ingr = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name_ingr}'


class Unit(models.Model):
    id_unit = models.AutoField(primary_key=True)
    name_unit = models.CharField(max_length=50)


class Connections(models.Model):
    id_con = models.AutoField(primary_key=True)
    id_recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    id_ingr = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    ingr_qty_unit = models.CharField(max_length=50)
    ingr_qty = models.FloatField(validators=[MinValueValidator(0.0, 'Количество должно быть больше ноля')], default=0.0)
    id_unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
