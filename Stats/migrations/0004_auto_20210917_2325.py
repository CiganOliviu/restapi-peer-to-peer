# Generated by Django 3.2.5 on 2021-09-17 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Stats', '0003_alter_staff_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='email_url',
            field=models.URLField(default=''),
        ),
        migrations.AddField(
            model_name='staff',
            name='linkedin_url',
            field=models.URLField(default=''),
        ),
    ]
