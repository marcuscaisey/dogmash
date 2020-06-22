from django import forms
from django.core.exceptions import ValidationError

from .models import Dog


class DogRatingForm(forms.Form):
    dog1 = forms.IntegerField()
    dog2 = forms.IntegerField()
    winner = forms.IntegerField()

    def clean(self):
        for field, value in self.cleaned_data.items():
            if not Dog.objects.filter(pk=value).exists():
                self.add_error(field, ValidationError("Dog doesn't exist.", code="invalid"))

        try:
            if self.cleaned_data["winner"] not in (self.cleaned_data["dog1"], self.cleaned_data["dog2"]):
                self.add_error("winner", ValidationError("Winner must be either dog1 or dog2.", code="invalid"))
        except KeyError:
            pass

    def save(self):
        dog1 = Dog.objects.get(pk=self.cleaned_data["dog1"])
        dog2 = Dog.objects.get(pk=self.cleaned_data["dog2"])

        winner, loser = (dog1, dog2) if self.cleaned_data["winner"] == dog1.pk else (dog2, dog1)

        winner.rating, loser.rating = calculate_elo(winner.rating, loser.rating)

        winner.save()
        loser.save()


def calculate_elo(winner_rating, loser_rating, k=40):
    """Return the Elo ratings of a winner and loser as a tuple."""
    R_1, R_2 = map(lambda x: 10 ** (x / 400), [winner_rating, loser_rating])
    E_1, E_2 = map(lambda x: x / (R_1 + R_2), [R_1, R_2])
    new_winner_rating = round(winner_rating + k * (1 - E_1))
    new_loser_rating = round(loser_rating - k * E_2)
    return new_winner_rating, new_loser_rating
