# Generated by Django 4.1.13 on 2024-02-26 21:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('open_source', '0003_opensourceproject_description_de_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='opensourceproject',
            name='description_de',
        ),
        migrations.RemoveField(
            model_name='opensourceproject',
            name='description_en',
        ),
        migrations.RemoveField(
            model_name='opensourceproject',
            name='description_ru',
        ),
        migrations.RemoveField(
            model_name='opensourceproject',
            name='job_title_de',
        ),
        migrations.RemoveField(
            model_name='opensourceproject',
            name='job_title_en',
        ),
        migrations.RemoveField(
            model_name='opensourceproject',
            name='job_title_ru',
        ),
    ]
