from django.db import models


class Movie(models.Model):

    name = models.CharField(max_length=128)
    description = models.TextField(default='', blank=True, null=True)
    year = models.CharField(null=True, blank=True, max_length=4)
    photo = models.ImageField(null=True, blank=True, default='blank.jpg', upload_to='plakaty')


    def __str__(self):
        return self.name_with_year()

    def name_with_year(self):
        return str(self.name) + ' (' + str(self.year) + ')'