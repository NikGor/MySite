# Generated by Django 5.0.1 on 2024-02-06 22:26

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_user_website'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='about_me',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
