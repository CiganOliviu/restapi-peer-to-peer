# Generated by Django 3.2.7 on 2021-10-17 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MathematicsDepartment', '0007_auto_20210914_2146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mathgroup',
            name='name',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
