# Generated by Django 4.1.13 on 2024-03-04 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_application', '0015_alter_jobapplication_german_level_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobapplication',
            name='other_benefits',
            field=models.TextField(blank=True, max_length=512, null=True),
        ),
    ]