from rest_framework import serializers
from AppLayout.models import HeroCard, HomeworkCard, ScheduleCard


class HeroCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeroCard
        fields = '__all__'


class HomeworkCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeworkCard
        fields = '__all__'


class ScheduleCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScheduleCard
        fields = '__all__'
