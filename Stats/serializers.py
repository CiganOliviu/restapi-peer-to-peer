from Stats.models import *
from Details.serializers import *


class ClientSerializers(serializers.ModelSerializer):
    high_school_profile = HighSchoolProfileSerializers(read_only=True)
    high_school = HighSchoolSerializers(read_only=True)
    city = TownSerializers(read_only=True)

    class Meta:
        model = Client
        fields = '__all__'


class TeacherSerializers(serializers.ModelSerializer):
    faculty = FacultieSerializers(read_only=True)
    city = TownSerializers(read_only=True)
    domain_expertise = DomainSerializers(read_only=True, many=True)

    class Meta:
        model = Teacher
        fields = '__all__'


class StaffSerializers(serializers.ModelSerializer):
    faculty = FacultieSerializers(read_only=True)
    city = TownSerializers(read_only=True)
    position = PositionSerializers(read_only=True)

    class Meta:
        model = Staff
        fields = '__all__'


class ExpenseSerializers(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = '__all__'


class IncomeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = '__all__'


class FeedbackSerializers(serializers.ModelSerializer):

    class Meta:
        model = Feedback
        fields = '__all__'


class TeacherGoalsSerializers(serializers.ModelSerializer):
    teacher = TeacherSerializers(read_only=True)

    class Meta:
        model = TeacherGoal
        fields = '__all__'


class StudentExpectationSerializers(serializers.ModelSerializer):
    student = ClientSerializers(read_only=True)

    class Meta:
        model = StudentExpectation
        fields = '__all__'
