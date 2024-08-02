# Generated by Django 5.0.6 on 2024-07-18 23:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="course",
            field=models.CharField(
                choices=[
                    ("WEB", "Web development with Python"),
                    ("BOOT", "Python Bootcamp"),
                    ("MATH", "Python for Mathematics"),
                    ("GAME", "Game development with Python"),
                ],
                default="WEB",
                max_length=4,
            ),
        ),
    ]