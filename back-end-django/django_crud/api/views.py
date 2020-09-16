from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework import permissions
from api.serializers import MovieSerializer
from api.models import Movie


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
