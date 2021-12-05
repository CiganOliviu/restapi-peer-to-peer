# Generated by Django 3.2.7 on 2021-11-30 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Contact', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='client_type',
            field=models.CharField(default=None, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(default=None, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='first_name',
            field=models.CharField(default=None, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='last_name',
            field=models.CharField(default=None, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.TextField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='subject',
            field=models.CharField(default=None, max_length=50, null=True),
        ),
    ]