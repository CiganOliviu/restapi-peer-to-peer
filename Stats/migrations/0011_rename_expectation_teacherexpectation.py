# Generated by Django 3.2.7 on 2021-10-20 16:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Stats', '0010_expectation'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Expectation',
            new_name='TeacherExpectation',
        ),
    ]