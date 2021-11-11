# Generated by Django 3.2.5 on 2021-08-29 17:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Stats', '0002_auto_20210829_1959'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('InformaticsDepartment', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Feedback',
        ),
        migrations.AlterModelOptions(
            name='schedule',
            options={'ordering': ['deadline']},
        ),
        migrations.AddField(
            model_name='group',
            name='client',
            field=models.ManyToManyField(default=None, to='Stats.Client'),
        ),
        migrations.AddField(
            model_name='group',
            name='name',
            field=models.CharField(default=None, max_length=15),
        ),
        migrations.AddField(
            model_name='group',
            name='responsible_teacher',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Stats.teacher'),
        ),
        migrations.AddField(
            model_name='homework',
            name='dated',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='homework',
            name='deadline',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='homework',
            name='file',
            field=models.FileField(blank=True, default='None', upload_to='homeworks/informatics'),
        ),
        migrations.AddField(
            model_name='homework',
            name='groups',
            field=models.ManyToManyField(default=None, to='InformaticsDepartment.Group'),
        ),
        migrations.AddField(
            model_name='homework',
            name='informatics_homework_slug',
            field=models.SlugField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='homework',
            name='optional',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='homework',
            name='posted_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='homework',
            name='teacher',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='homework',
            name='tips',
            field=models.TextField(blank=True, default='None'),
        ),
        migrations.AddField(
            model_name='homework',
            name='title',
            field=models.CharField(default=None, max_length=150, unique=True),
        ),
        migrations.AddField(
            model_name='schedule',
            name='course_title',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='schedule',
            name='dated',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='schedule',
            name='deadline',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='schedule',
            name='group',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='InformaticsDepartment.group'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='posted_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='schedule',
            name='teacher',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]