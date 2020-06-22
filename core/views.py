import random

from django.shortcuts import render
from django.urls import reverse_lazy

from .models import Dog
from django.views.generic import CreateView


def home(request):
    """Render the home page template with two random Dog objects."""
    dogs = random.sample(tuple(Dog.objects.all()), k=2)
    return render(request, "core/home.html", {"dogs": dogs})


class UploadView(CreateView):
    model = Dog
    fields = ("image",)
    template_name = "core/upload.html"
    success_url = reverse_lazy("core:upload")
