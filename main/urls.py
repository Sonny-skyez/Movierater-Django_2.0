from django.urls import path
from .views import wszystkie_filmy, nowy_film, edytuj_film, usun_film

from django.urls import include, path
from rest_framework import routers
from .views import UserViewSet, MovieViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'movies', MovieViewSet)


urlpatterns = [
    path('filmy/', wszystkie_filmy, name = "wszystkie_filmy"),
    path('nowy/', nowy_film, name = 'nowy_film'),
    path('edytuj/<int:id>/', edytuj_film, name = 'edytuj_film'),
    path('usun/<int:id>/', usun_film, name = 'usun_film'),
    path('', include(router.urls)),
    path('', include(router.urls)),
]


# path('', include(router.urls)),