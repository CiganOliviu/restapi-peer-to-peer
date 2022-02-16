from rest_framework import serializers
from AppLayout.models import HeroCard, HomeworkCard, ScheduleCard, ContentSection, ContentWithImagesSection, HomeContent


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


class ContentSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentSection
        fields = '__all__'


class ContentWithImagesSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentWithImagesSection
        fields = '__all__'


class HomeContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeContent
        fields = '__all__'
