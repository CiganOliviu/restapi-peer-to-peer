# Generated by Django 3.2.7 on 2022-02-15 21:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AppLayout', '0006_contentsection_contentwithimagessection_homecontent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homecontent',
            name='section_with_images_content',
        ),
        migrations.AddField(
            model_name='homecontent',
            name='section_one_with_images_content',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='section_images_one', to='AppLayout.contentwithimagessection'),
        ),
        migrations.AddField(
            model_name='homecontent',
            name='section_three_with_images_content',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='section_images_three', to='AppLayout.contentwithimagessection'),
        ),
        migrations.AddField(
            model_name='homecontent',
            name='section_two_with_images_content',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='section_images_two', to='AppLayout.contentwithimagessection'),
        ),
        migrations.AlterField(
            model_name='homecontent',
            name='section_one_title_content',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='section_one', to='AppLayout.contentsection'),
        ),
        migrations.AlterField(
            model_name='homecontent',
            name='section_two_title_content',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='section_two', to='AppLayout.contentsection'),
        ),
    ]
