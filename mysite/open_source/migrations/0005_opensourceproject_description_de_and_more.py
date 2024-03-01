# Generated by Django 4.1.13 on 2024-02-29 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('open_source', '0004_remove_opensourceproject_description_de_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='opensourceproject',
            name='description_de',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='opensourceproject',
            name='description_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='opensourceproject',
            name='job_title_de',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='opensourceproject',
            name='job_title_en',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='opensourceproject',
            name='name_de',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='opensourceproject',
            name='name_en',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
