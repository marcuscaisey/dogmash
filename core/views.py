import random

from django.shortcuts import render

from .models import Dog


def home(request):
    """Render the home page template with two random Dog objects."""
    dogs = random.sample(tuple(Dog.objects.all()), k=2)
    return render(request, "core/home.html", {"dogs": dogs})
