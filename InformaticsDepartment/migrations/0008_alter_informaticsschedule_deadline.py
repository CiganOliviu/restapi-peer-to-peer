# Generated by Django 3.2.5 on 2021-09-12 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InformaticsDepartment', '0007_alter_informaticsschedule_deadline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='informaticsschedule',
            name='deadline',
            field=models.DateTimeField(),
        ),
    ]