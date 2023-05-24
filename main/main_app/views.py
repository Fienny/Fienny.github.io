from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *


class UsersViewset(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    http_method_names = ['post']


class PerevalAddedViewset(viewsets.ModelViewSet):
    queryset = PerevalAdded.objects.all()
    serializer_class = PerevalAdddedSerializer
    http_method_names = ['post']


class CoordinatesViewset(viewsets.ModelViewSet):
    queryset = Coordinates.objects.all()
    serializer_class = CoordinatesSerializer
    http_method_names = ['post']


class ActivityViewset(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    http_method_names = ['post']


class PerevalAreasViewset(viewsets.ModelViewSet):
    queryset = PerevalAreas.objects.all()
    serializer_class = PerevalAreasSerializer
    http_method_names = ['post']


class PerevalImagesViewset(viewsets.ModelViewSet):
    queryset = PerevalImages.objects.all()
    serializer_class = PerevalImagesSerializer
    http_method_names = ['post']
