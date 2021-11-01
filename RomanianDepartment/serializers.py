from .models import *
from Stats.serializers import *


class RomanianGroupSerializers(serializers.ModelSerializer):

    responsible_teacher = TeacherSerializers(read_only=True)
    client = ClientSerializers(many=True)

    class Meta:
        model = RomanianGroup
        fields = '__all__'


class RomanianScheduleSerializers(serializers.ModelSerializer):

    teacher = TeacherSerializers(read_only=True)
    group = RomanianGroupSerializers(many=True)

    class Meta:
        model = RomanianSchedule
        fields = '__all__'


class RomanianHomeworkSerializers(serializers.ModelSerializer):

    teacher = TeacherSerializers(read_only=True)
    groups = RomanianGroupSerializers(many=True)

    class Meta:
        model = RomanianHomework
        fields = '__all__'
