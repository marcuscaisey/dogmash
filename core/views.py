import random

from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from .forms import DogRatingForm
from .models import Dog


def home(request):
    """
    GET
        Render the home page template with two random Dog objects.

        Context:
            - dogs: A list of two Dog objects.

    POST
        Process the form data from a submitted DogRatingForm and redirect back
        to the home page.
    """
    if request.method == "POST":
        form = DogRatingForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("core:home")

    dogs = random.sample(tuple(Dog.objects.all()), k=2)
    return render(request, "core/home.html", {"dogs": dogs})


class RankingsView(ListView):
    template_name = "core/rankings.html"
    model = Dog
    ordering = "-rating"
    paginate_by = 5


class UploadView(CreateView):
    model = Dog
    fields = ("image",)
    template_name = "core/upload.html"
    success_url = reverse_lazy("core:upload")
