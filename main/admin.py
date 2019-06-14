from django.contrib import admin
from .models import Movie, Review, Aktor

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    # fields = ('name', 'description', 'year')
    list_display = ('name', 'description', 'year', 'released')
    list_filter = ('year', 'released')
    search_fields = ('name', 'description')


admin.site.register(Review)
admin.site.register(Aktor)