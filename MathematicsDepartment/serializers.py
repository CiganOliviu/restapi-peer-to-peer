from rest_framework import serializers
from MathematicsDepartment.models import (
    MathGroup,
    MathSchedule,
    MathHomework
)
from Stats.serializers import (
    ClientSerializers,
    TeacherSerializers,
)


class MathematicsGroupSerializers(serializers.ModelSerializer):

    responsible_teacher = TeacherSerializers(read_only=True)
    client = ClientSerializers(many=True)

    class Meta:
        model = MathGroup
        fields = '__all__'


class MathematicsScheduleSerializers(serializers.ModelSerializer):

    teacher = TeacherSerializers(read_only=True)
    group = MathematicsGroupSerializers(many=True)

    class Meta:
        model = MathSchedule
        fields = '__all__'


class MathematicsHomeworkSerializers(serializers.ModelSerializer):

    teacher = TeacherSerializers(read_only=True)
    groups = MathematicsGroupSerializers(many=True)

    class Meta:
        model = MathHomework
        fields = '__all__'
