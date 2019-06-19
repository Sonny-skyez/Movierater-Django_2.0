from django.db import models
from multiselectfield import MultiSelectField
from author.decorators import with_author


CHOICES = (('Yes', 'Polecam!'),
           ('No', 'Odradzam!')
           )


@with_author
class Movie(models.Model):

    name = models.CharField(max_length=128)
    reccomendation = MultiSelectField(choices=CHOICES, default='', max_choices=1, null=True)
    description = models.TextField(default='', blank=True, null=True)
    year = models.CharField(null=True, blank=True, max_length=4)
    photo = models.ImageField(null=True, blank=True, default='blank.jpg')


    def __str__(self):
        return self.name_with_year()


    def name_with_year(self):
        if self.year:
            return str(self.name) + ' (' + str(self.year) + ')'
        else:
            return str(self.name)


    def reccomend_movie(self):
        if self.reccomendation:
            return self.reccomendation