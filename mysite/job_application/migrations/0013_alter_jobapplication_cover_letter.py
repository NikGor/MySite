# Generated by Django 4.1.13 on 2024-03-04 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_application', '0012_alter_jobapplication_cover_letter_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobapplication',
            name='cover_letter',
            field=models.TextField(blank=True, null=True),
        ),
    ]
