# Generated by Django 4.1.13 on 2024-03-02 11:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job_application', '0002_jobapplication_german_level_jobapplication_is_remote_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobapplication',
            name='final_decision',
        ),
        migrations.RemoveField(
            model_name='jobapplication',
            name='onsite_interview_done',
        ),
        migrations.RemoveField(
            model_name='jobapplication',
            name='onsite_interview_invited',
        ),
        migrations.RemoveField(
            model_name='jobapplication',
            name='phone_interview_done',
        ),
        migrations.RemoveField(
            model_name='jobapplication',
            name='phone_interview_invited',
        ),
        migrations.RemoveField(
            model_name='jobapplication',
            name='responded',
        ),
    ]
