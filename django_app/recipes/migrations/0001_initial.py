# Generated by Django 4.1.6 on 2023-02-01 16:52

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id_ingr', models.AutoField(primary_key=True, serialize=False)),
                ('name_ingr', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id_recipe', models.AutoField(primary_key=True, serialize=False)),
                ('name_recipe', models.CharField(max_length=200)),
                ('text_recipe', models.TextField()),
                ('vegetarian', models.BooleanField(default=0)),
                ('calories', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0, 'Калорий должно быть >= 0')])),
                ('protein', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0, 'Белка должно быть >= 0')])),
                ('fat', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0, 'Жиров должно быть >= 0')])),
                ('carbo', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0, 'Углеводов должно быть >= 0')])),
                ('portions', models.IntegerField(validators=[django.core.validators.MinValueValidator(0, 'Порций должно быть больше ноля')])),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id_unit', models.AutoField(primary_key=True, serialize=False)),
                ('name_unit', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Connections',
            fields=[
                ('id_con', models.AutoField(primary_key=True, serialize=False)),
                ('ingr_qty_unit', models.CharField(max_length=50)),
                ('ingr_qty', models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(0.0, 'Количество должно быть больше ноля')])),
                ('id_ingr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipes.ingredient')),
                ('id_recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipes.recipe')),
                ('id_unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipes.unit')),
            ],
        ),
    ]
