# Generated by Django 5.0.2 on 2024-02-19 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipies', '0002_remove_recipe_ingredients_remove_recipe_instructions'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='ingredients',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='instructions',
            field=models.TextField(null=True),
        ),
    ]