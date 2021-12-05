from django.contrib.auth.models import User
from Details.models import *


class Client(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, name='user', default=None, blank=False, null=True)
    first_name = models.CharField(max_length=50, default=None, blank=True, null=True)
    last_name = models.CharField(max_length=50, default=None, blank=True, null=True)
    email = models.EmailField(max_length=50, default=None, blank=True, null=True)
    high_school_profile = models.ForeignKey(HighSchoolProfile, on_delete=models.CASCADE, default=None, blank=False,
                                            null=True)
    high_school = models.ForeignKey(HighSchool, on_delete=models.CASCADE, default=None, blank=False, null=True)
    city = models.ForeignKey(Town, on_delete=models.CASCADE, default=1, blank=False, null=True)
    phone_number = models.CharField(max_length=100, default="07 XXX XXX XX", blank=False)

    def __str__(self):
        return str(self.user)


class Teacher(models.Model):
    profile = models.ImageField(upload_to='teachers-profile-image/', default='teachers-profile-image/default.jpg')
    user = models.OneToOneField(User, on_delete=models.CASCADE, name='user', default=None, blank=False)
    first_name = models.CharField(max_length=50, default=None, blank=False)
    last_name = models.CharField(max_length=50, default=None, blank=False)
    age = models.CharField(max_length=2, default=None, blank=False)
    email = models.EmailField(max_length=50, default=None, blank=False)
    phone_number = models.CharField(max_length=100, default="07 XXX XXX XX", blank=False)
    faculty = models.ForeignKey(Facultie, on_delete=models.CASCADE, default=None, blank=False)
    city = models.ForeignKey(Town, on_delete=models.CASCADE, default=1, blank=False)
    domain_expertise = models.ManyToManyField(Domain, default=None, blank=False)
    description = models.TextField(default=None, blank=True)
    one_prop_description = models.CharField(max_length=200, default='One Prop Description', blank=False)

    def __str__(self):
        return str(self.first_name + " " + self.last_name)


class Staff(models.Model):
    id = models.IntegerField(primary_key=True)
    profile = models.ImageField(upload_to='staff-profile-image/', default='teachers-profile-image/default.jpg')
    user = models.OneToOneField(User, on_delete=models.CASCADE, name='user', default=None, blank=False)
    first_name = models.CharField(max_length=100, default=None, blank=False)
    last_name = models.CharField(max_length=100, default=None, blank=False)
    age = models.CharField(max_length=2, default=None, blank=False)
    email = models.EmailField(max_length=100, default=None, blank=False)
    faculty = models.ForeignKey(Facultie, on_delete=models.CASCADE, default=None, blank=False)
    city = models.ForeignKey(Town, on_delete=models.CASCADE, default=1, blank=False)
    preview = models.TextField(default="None", blank=False)
    description = models.TextField(default=None, blank=False)
    position = models.ForeignKey(Position, on_delete=models.CASCADE, name='position', default=None, blank=False)
    linkedin_url = models.URLField(default='')
    email_url = models.CharField(max_length=150, default='')

    def __str__(self):
        return str(self.user)


class Expense(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE, default=None, blank=False)
    scope = models.CharField(max_length=100, default=None, blank=False)
    expense = models.IntegerField(default=0)

    def __str__(self):
        return str(self.staff)


class Income(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE, default=None, blank=False)
    income = models.IntegerField(default=0)

    def __str__(self):
        return str(self.staff)


class Feedback(models.Model):
    title = models.CharField(max_length=150, default='', blank=False)
    targetTeacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    message = models.TextField(default='', unique=True)
    posted_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-posted_on']

    def __str__(self):
        return self.title


class TeacherGoal(models.Model):
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, name='teacher', default=None, blank=True)
    title = models.CharField(max_length=150, default='', blank=False)
    log = models.TextField(default='', unique=True)
    posted_on = models.DateField(auto_now_add=True)
    deadline = models.DateField(blank=True)
    done = models.BooleanField(default=False)

    class Meta:
        ordering = ['-posted_on']

    def __str__(self):
        return self.title


class StudentExpectation(models.Model):
    student = models.ForeignKey(Client, on_delete=models.CASCADE, name='student', default=None, blank=True)
    title = models.CharField(max_length=150, default='', blank=False)
    log = models.TextField(default='', unique=True)
    posted_on = models.DateField(auto_now_add=True)
    deadline = models.DateField(blank=True)
    done = models.BooleanField(default=False)

    class Meta:
        ordering = ['-posted_on']

    def __str__(self):
        return self.title
