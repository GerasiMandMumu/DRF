from rest_framework import serializers

from dota.models import Hero


class HeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hero
        fields = ('title', 'cat_id')