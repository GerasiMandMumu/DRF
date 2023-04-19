from django.shortcuts import render
from rest_framework import generics

from dota.models import Hero

from dota.serializers import HeroSerializer


class HeroAPIView(generics.ListAPIView):
    queryset = Hero.objects.all()
    serializer_class = HeroSerializer