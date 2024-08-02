# Generated by Django 5.0.6 on 2024-08-02 01:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0011_rename_imgname_post_imgname1_remove_post_image_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="image1",
            field=models.ImageField(
                default="/static/images/default.png", upload_to="images/"
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="image2",
            field=models.ImageField(
                default="/static/images/default.png", upload_to="images/"
            ),
        ),
    ]