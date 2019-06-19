from django.contrib import admin
from .models import Movie

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    # fields = ('name', 'description', 'year')
    list_display = ('name', 'year', 'reccomendation', 'author', 'updated_by')
    list_filter = ['year','reccomendation', 'name', 'author']
    search_fields = ('name', 'description')


admin.site.site_url = "/main/filmy"