# Generated by Django 3.2.5 on 2021-09-12 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InformaticsDepartment', '0004_auto_20210829_2059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='informaticsschedule',
            name='posted_on',
            field=models.DateField(auto_now_add=True),
        ),
    ]
