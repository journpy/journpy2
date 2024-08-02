# Generated by Django 5.0.6 on 2024-08-02 00:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0010_alter_post_image_alter_post_image2_alter_post_slug"),
    ]

    operations = [
        migrations.RenameField(
            model_name="post",
            old_name="imgname",
            new_name="imgname1",
        ),
        migrations.RemoveField(
            model_name="post",
            name="image",
        ),
        migrations.AddField(
            model_name="post",
            name="image1",
            field=models.ImageField(default=1, upload_to="images/"),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="post",
            name="image2",
            field=models.ImageField(upload_to="images/"),
        ),
    ]
