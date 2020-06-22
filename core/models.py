from django.db import models
from django.db.models import Count, Q


class Dog(models.Model):
    rating = models.DecimalField(decimal_places=3, max_digits=7)
    image = models.ImageField(upload_to="uploads/%Y/%m/%d/", width_field="width", height_field="height")

    def __str__(self):
        return f"pk={self.pk}, rating={self.rating}"

    @property
    def rank(self):
        # Your rank is the number of distinct ratings greater than your rating + 1.
        return Dog.objects.aggregate(rank=Count("rating", filter=Q(rating__gt=self.rating), distinct=True) + 1)["rank"]
