from .views import wszystkie_filmy, nowy_film, edytuj_film, usun_film

from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers


router = routers.DefaultRouter()


urlpatterns = [
    path('filmy/', wszystkie_filmy, name = "wszystkie_filmy"),
    path('nowy/', nowy_film, name = 'nowy_film'),
    path('edytuj/<int:id>/', edytuj_film, name = 'edytuj_film'),
    path('usun/<int:id>/', usun_film, name = 'usun_film'),
    url(r'^', include(router.urls)),
]



# path('', include(router.urls)),