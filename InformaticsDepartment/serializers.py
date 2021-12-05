from rest_framework import serializers
from .models import *
from Stats.serializers import (
    TeacherSerializers,
    ClientSerializers
)


class InformaticsGroupSerializers(serializers.ModelSerializer):

    responsible_teacher = TeacherSerializers(read_only=True)
    client = ClientSerializers(many=True)

    class Meta:
        model = InformaticsGroup
        fields = '__all__'


class InformaticsScheduleSerializers(serializers.ModelSerializer):

    teacher = TeacherSerializers(read_only=True)
    group = InformaticsGroupSerializers(read_only=True)

    class Meta:
        model = InformaticsSchedule
        fields = '__all__'


class InformaticsHomeworkSerializers(serializers.ModelSerializer):

    teacher = TeacherSerializers(read_only=True)
    groups = InformaticsGroupSerializers(many=True)

    class Meta:
        model = InformaticsHomework
        fields = '__all__'
