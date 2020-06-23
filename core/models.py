from django.db import models
from django.db.models import Count, Q

from PIL import Image


class Dog(models.Model):
    rating = models.IntegerField(default=1000)
    image = models.ImageField(upload_to="uploads/")

    def __str__(self):
        return f"pk={self.pk}, rating={self.rating}"

    @property
    def rank(self):
        # Your rank is the number of distinct ratings greater than your rating + 1.
        return Dog.objects.aggregate(rank=Count("rating", filter=Q(rating__gt=self.rating), distinct=True) + 1)["rank"]

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.image.width > 300 or self.image.height > 400:
            image = Image.open(self.image.path)

            if image.width > 300:
                aspect_ratio = self.image.width / self.image.height
                image = image.resize((300, round(300 / aspect_ratio)))

            if image.height > 400:
                image = image.crop((0, image.height - 400, 300, image.height))

            image.save(self.image.path)

