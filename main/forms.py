from django.forms import ModelForm
from .models import Movie

class MovieForm(ModelForm):

    class Meta:
        model = Movie
        fields = ['name', 'reccomendation', 'description', 'year', 'photo']     # lub exclude - te których ma nie być w projekcie.

