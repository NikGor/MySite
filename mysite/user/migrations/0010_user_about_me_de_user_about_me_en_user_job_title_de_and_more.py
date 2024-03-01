# Generated by Django 4.1.13 on 2024-02-26 22:05

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_remove_user_about_me_de_remove_user_about_me_en_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='about_me_de',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='about_me_en',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='job_title_de',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='job_title_en',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
