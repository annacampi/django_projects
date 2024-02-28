from django.db import models

class Recipe(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    ingredients = models.TextField(null=True)
    instructions = models.TextField(null=True)
    image = models.ImageField(null=True, upload_to='images/')

    def __str__(self):
        return f"{self.title}"