import io

from PIL import Image
from django.core.files.base import ContentFile
from django.db import models
from django.db.models import Count, Q


class Dog(models.Model):
    rating = models.IntegerField(default=1000)
    image = models.ImageField(upload_to="uploads/")
    thumbnail = models.ImageField(upload_to="uploads/thumbnails/")

    def __str__(self):
        return f"pk={self.pk}, rating={self.rating}"

    @property
    def rank(self):
        # Your rank is the number of distinct ratings greater than your rating + 1.
        return Dog.objects.aggregate(rank=Count("rating", filter=Q(rating__gt=self.rating), distinct=True) + 1)["rank"]

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self._save_thumbnail(64, 64)
        self._resize_image(300, 400)

    def _save_thumbnail(self, width):
        if self.thumbnail:
            return

        with self.image.open() as f:
            image = Image.open(f)
            image.load()

        name = self.image.name.split("/")[-1]
        format = image.format

        if image.width > image.height:
            crop_start = (image.width - image.height) // 2
            image = image.crop((crop_start, 0, crop_start + image.height, image.height))
        elif image.width < image.height:
            crop_start = (image.height - image.width) // 2
            image = image.crop((0, crop_start, image.width, crop_start + image.width))

        image.thumbnail((width, width))

        image_bytes = io.BytesIO()
        image.save(image_bytes, format)
        image_bytes.seek(0)

        self.thumbnail.save(name, ContentFile(image_bytes.read()))

    def _resize_image(self, width, height):
        if self.image.width < width and self.image.height < height:
            return

        with self.image.open() as f:
            image = Image.open(f)
            image.load()

        if image.width > width:
            aspect_ratio = self.image.width / self.image.height
            image = image.resize((width, round(width / aspect_ratio)))

        if image.height > height:
            image = image.crop((0, image.height - height, width, image.height))

        with self.image.open("wb"):
            image.save(self.image)
