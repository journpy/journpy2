# Generated by Django 5.0.6 on 2024-08-02 01:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0013_alter_post_image1_alter_post_image2"),
    ]

    operations = [
        migrations.RenameField(
            model_name="post",
            old_name="date_modified",
            new_name="date_added",
        ),
        migrations.RenameField(
            model_name="post",
            old_name="imgname1",
            new_name="imgname",
        ),
        migrations.RemoveField(
            model_name="post",
            name="date_created",
        ),
        migrations.RemoveField(
            model_name="post",
            name="image1",
        ),
        migrations.AddField(
            model_name="post",
            name="image",
            field=models.ImageField(blank=True, upload_to="images/"),
        ),
        migrations.AlterField(
            model_name="post",
            name="image2",
            field=models.ImageField(blank=True, upload_to="images/"),
        ),
    ]
