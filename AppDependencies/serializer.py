from rest_framework import serializers
from AppDependencies.models import HeroCard


class HeroCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeroCard
        fields = '__all__'
