import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from dota.models import Hero

# class HeroModel:
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content

class HeroSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    content = serializers.CharField()
    time_create = serializers.DateTimeField()
    time_update = serializers.DateTimeField()
    cat_id = serializers.IntegerField()


# def encode():
#     model = HeroModel('Antimage', 'Content: Antimage')
#     model_sr = HeroSerializer(model)
#     print(model_sr.data, type(model_sr.data), sep='\n')
#     json = JSONRenderer().render(model_sr.data)
#     print(json)
#
# def decode():
#     stream = io.BytesIO(b'{"title":"Antimage","content":"Content: Antimage"}')
#     data = JSONParser().parse(stream)
#     serializer = HeroSerializer(data=data)
#     serializer.is_valid()
#     print(serializer.validated_data)