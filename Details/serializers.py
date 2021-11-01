from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *


class DomainSerializers(serializers.ModelSerializer):
    class Meta:
        model = Domain
        fields = '__all__'


class HighSchoolProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = HighSchoolProfile
        fields = '__all__'


class TownSerializers(serializers.ModelSerializer):
    class Meta:
        model = Town
        fields = '__all__'


class UniversitieSerializers(serializers.ModelSerializer):
    town = TownSerializers(read_only=True)

    class Meta:
        model = Universitie
        fields = '__all__'


class FacultieSerializers(serializers.ModelSerializer):
    university = UniversitieSerializers(read_only=True)

    class Meta:
        model = Facultie
        fields = '__all__'


class PositionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = '__all__'


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
