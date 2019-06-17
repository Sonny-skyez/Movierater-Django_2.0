from django.contrib import admin
from .models import Movie

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    # fields = ('name', 'description', 'year')
    list_display = ('name', 'description', 'year')
    list_filter = ['year','reccomendation', 'name']
    search_fields = ('name', 'description')


admin.site.site_url = "/main/filmy"