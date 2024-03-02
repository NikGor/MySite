# Generated by Django 4.1.13 on 2024-03-04 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_application', '0014_jobapplication_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobapplication',
            name='german_level',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='required_experience',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='salary_range',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='vacation_days',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]