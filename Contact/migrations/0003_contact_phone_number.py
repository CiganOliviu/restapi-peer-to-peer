# Generated by Django 3.2.7 on 2021-12-03 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Contact', '0002_auto_20211130_2046'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='phone_number',
            field=models.CharField(default='07 XXX XXX XX', max_length=50),
        ),
    ]
