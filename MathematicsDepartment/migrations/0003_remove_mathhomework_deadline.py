# Generated by Django 3.2.5 on 2021-09-14 18:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MathematicsDepartment', '0002_auto_20210829_2058'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mathhomework',
            name='deadline',
        ),
    ]
