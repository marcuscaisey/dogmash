from django.db import models


class Dog(models.Model):
    rating = models.DecimalField(decimal_places=3, max_digits=7)
    image = models.ImageField()
