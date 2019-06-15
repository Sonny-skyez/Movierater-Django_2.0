from django.contrib import admin
from .models import Movie

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    # fields = ('name', 'description', 'year')
    list_display = ('name', 'description', 'year', 'released')
    list_filter = ('year', 'released')
    search_fields = ('name', 'description')