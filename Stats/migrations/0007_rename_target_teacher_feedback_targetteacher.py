# Generated by Django 3.2.5 on 2021-09-22 19:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Stats', '0006_alter_feedback_message'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='target_teacher',
            new_name='targetTeacher',
        ),
    ]
