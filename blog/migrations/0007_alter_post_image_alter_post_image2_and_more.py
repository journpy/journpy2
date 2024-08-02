# Generated by Django 5.0.6 on 2024-08-01 23:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0006_rename_date_added_post_date_modified_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="image",
            field=models.ImageField(blank=True, default=1, upload_to="images/"),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="post",
            name="image2",
            field=models.ImageField(blank=True, default=1, upload_to="images/"),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="post",
            name="imgname",
            field=models.CharField(blank=True, default=1, max_length=250),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="post",
            name="imgname2",
            field=models.CharField(blank=True, default=1, max_length=250),
            preserve_default=False,
        ),
    ]
