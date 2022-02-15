# Generated by Django 3.2.7 on 2022-02-15 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppLayout', '0004_homeworkcard_schedulecard'),
    ]

    operations = [
        migrations.AlterField(
            model_name='herocard',
            name='image',
            field=models.ImageField(default='app-layout/hero-card-wallpaper/default.jpg', upload_to='app-layout/hero-card-wallpapers/'),
        ),
        migrations.AlterField(
            model_name='homeworkcard',
            name='image',
            field=models.ImageField(default='app-layout/homework-card-wallpapers/default.jpg', upload_to='app-layout/homework-card-wallpapers/'),
        ),
        migrations.AlterField(
            model_name='schedulecard',
            name='image',
            field=models.ImageField(default='app-layout/schedule-card-wallpapers/default.jpg', upload_to='app-layout/schedule-card-wallpapers/'),
        ),
    ]
