from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Movie, ExtraInfo


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'url', 'username', 'email')


class InfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ExtraInfo
        fields = ('czas_trwania', 'rodzaj')


class MovieSerializer(serializers.ModelSerializer):

    info = InfoSerializer(many=False)

    class Meta:
        model = Movie
        fields = ('id', 'name', 'description', 'year', 'released', 'info')