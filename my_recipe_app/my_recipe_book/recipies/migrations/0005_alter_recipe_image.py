# Generated by Django 5.0.2 on 2024-02-20 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipies', '0004_recipe_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=models.ImageField(null=True, upload_to='images'),
        ),
    ]
