import datetime
from AppDependencies import update_model_content
from Stats.models import *


class MathGroup(models.Model):
    client = models.ManyToManyField(Client, default=None, blank=False)
    name = models.CharField(max_length=100, default=None, blank=False)
    responsible_teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, default=1, blank=False)

    def __str__(self):
        return self.name


class MathSchedule(models.Model):
    course_title = models.CharField(max_length=100, default=None, blank=False)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, name='teacher', default=None, blank=True)
    group = models.ForeignKey(MathGroup, on_delete=models.CASCADE, default=None, blank=False,
                              null=True)
    deadline_date = models.DateField(default=datetime.date.today)
    deadline_hour = models.TimeField(default=datetime.time(10, 0))
    dated = models.BooleanField(default=False, )
    posted_on = models.DateField(default=datetime.date.today)

    class Meta:
        ordering = ['deadline_date']

    def save(self, *args, **kwargs):
        update_model_content.fetch_schedule_model(MathSchedule)

        super(MathSchedule, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.teacher)


class MathHomework(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, name='teacher', default=None, blank=True,
                             null=True)
    title = models.CharField(max_length=150, default=None, blank=False, unique=True)
    groups = models.ManyToManyField(MathGroup, default=None, blank=False)
    file = models.FileField(upload_to='homeworks/informatics', default='None', blank=True)
    tips = models.TextField(default='None', blank=True)
    optional = models.BooleanField(default=False)
    deadline_date = models.DateField(default=datetime.date.today)
    deadline_hour = models.TimeField(default=datetime.time(10, 0))
    dated = models.BooleanField(default=False)
    posted_on = models.DateField(default=datetime.date.today)

    def save(self, *args, **kwargs):
        update_model_content.fetch_homework_model(MathHomework)

        super(MathHomework, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
