# Generated by Django 3.2.5 on 2021-09-12 20:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InformaticsDepartment', '0017_remove_informaticshomework_posted_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='informaticshomework',
            name='posted_on',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
