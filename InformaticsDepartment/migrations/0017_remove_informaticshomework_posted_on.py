# Generated by Django 3.2.5 on 2021-09-12 20:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('InformaticsDepartment', '0016_auto_20210912_2338'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='informaticshomework',
            name='posted_on',
        ),
    ]
