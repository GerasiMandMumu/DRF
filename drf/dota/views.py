from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from dota.models import Hero

from dota.serializers import HeroSerializer


class HeroAPIView(APIView):
    def get(self, request):
        lst = Hero.objects.all()
        return Response({'posts': HeroSerializer(lst, many=True).data})

    def post(self, request):
        serializer = HeroSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        post_new = Hero.objects.create(
            title=request.data['title'],
            content=request.data['content'],
            cat_id=request.data['cat_id']
        )
        return Response({'post': HeroSerializer(post_new).data})

# class HeroAPIView(generics.ListAPIView):
#     queryset = Hero.objects.all()
#     serializer_class = HeroSerializer