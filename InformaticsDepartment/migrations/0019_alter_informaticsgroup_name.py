# Generated by Django 3.2.7 on 2021-10-17 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InformaticsDepartment', '0018_informaticshomework_posted_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='informaticsgroup',
            name='name',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
