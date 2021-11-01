# Generated by Django 3.2.7 on 2021-10-07 21:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Stats', '0007_rename_target_teacher_feedback_targetteacher'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='feedback',
            options={'ordering': ['-posted_on']},
        ),
        migrations.AddField(
            model_name='feedback',
            name='posted_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
