from rest_framework import serializers
from .models import *


class HeroCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeroCard
        fields = '__all__'
