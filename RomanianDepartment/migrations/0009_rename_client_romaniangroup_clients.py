# Generated by Django 3.2.7 on 2022-01-27 18:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RomanianDepartment', '0008_alter_romanianhomework_file'),
    ]

    operations = [
        migrations.RenameField(
            model_name='romaniangroup',
            old_name='client',
            new_name='clients',
        ),
    ]
