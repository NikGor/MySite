# Generated by Django 4.1.7 on 2023-12-19 21:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("education", "0002_education_url"),
    ]

    operations = [
        migrations.AddField(
            model_name="education",
            name="order",
            field=models.IntegerField(default=0),
        ),
    ]
