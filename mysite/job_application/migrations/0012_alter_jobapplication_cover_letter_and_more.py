# Generated by Django 4.1.13 on 2024-03-04 00:13

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job_application', '0011_alter_jobapplication_vacation_days'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobapplication',
            name='cover_letter',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='cv_intro',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
