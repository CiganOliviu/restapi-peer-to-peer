# Generated by Django 3.2.5 on 2021-08-29 16:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Details', '0002_auto_20210829_1953'),
        ('Stats', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='city',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='Details.town'),
        ),
        migrations.AddField(
            model_name='client',
            name='email',
            field=models.EmailField(blank=True, default=None, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='first_name',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='high_school_profile',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Details.highschoolprofile'),
        ),
        migrations.AddField(
            model_name='client',
            name='last_name',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='user',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='expense',
            name='expense',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='expense',
            name='scope',
            field=models.CharField(default=None, max_length=25),
        ),
        migrations.AddField(
            model_name='expense',
            name='staff',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Stats.staff'),
        ),
        migrations.AddField(
            model_name='income',
            name='income',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='income',
            name='staff',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Stats.staff'),
        ),
        migrations.AddField(
            model_name='staff',
            name='age',
            field=models.CharField(default=None, max_length=2),
        ),
        migrations.AddField(
            model_name='staff',
            name='city',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Details.town'),
        ),
        migrations.AddField(
            model_name='staff',
            name='description',
            field=models.TextField(default=None),
        ),
        migrations.AddField(
            model_name='staff',
            name='email',
            field=models.EmailField(default=None, max_length=50),
        ),
        migrations.AddField(
            model_name='staff',
            name='faculty',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Details.facultie'),
        ),
        migrations.AddField(
            model_name='staff',
            name='first_name',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AddField(
            model_name='staff',
            name='last_name',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AddField(
            model_name='staff',
            name='position',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Details.position'),
        ),
        migrations.AddField(
            model_name='staff',
            name='preview',
            field=models.TextField(default='None'),
        ),
        migrations.AddField(
            model_name='staff',
            name='profile',
            field=models.ImageField(default='teachers-profile-image/default.jpg', upload_to='staff-profile-image/'),
        ),
        migrations.AddField(
            model_name='staff',
            name='user',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='teacher',
            name='age',
            field=models.CharField(default=None, max_length=2),
        ),
        migrations.AddField(
            model_name='teacher',
            name='city',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Details.town'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='description',
            field=models.TextField(blank=True, default=None),
        ),
        migrations.AddField(
            model_name='teacher',
            name='domain_expertise',
            field=models.ManyToManyField(default=None, to='Details.Domain'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='email',
            field=models.EmailField(default=None, max_length=50),
        ),
        migrations.AddField(
            model_name='teacher',
            name='faculty',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Details.facultie'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='first_name',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AddField(
            model_name='teacher',
            name='last_name',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AddField(
            model_name='teacher',
            name='one_prop_description',
            field=models.CharField(default='One Prop Description', max_length=200),
        ),
        migrations.AddField(
            model_name='teacher',
            name='phone_number',
            field=models.CharField(default='07 XXX XXX XX', max_length=100),
        ),
        migrations.AddField(
            model_name='teacher',
            name='profile',
            field=models.ImageField(default='teachers-profile-image/default.jpg', upload_to='teachers-profile-image/'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='user',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]