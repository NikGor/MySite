# Generated by Django 4.1.13 on 2024-02-29 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0005_remove_education_description_de_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='description_de',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='education',
            name='description_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='education',
            name='faculty_de',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='education',
            name='faculty_en',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='education',
            name='school_de',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='education',
            name='school_en',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
