# Generated by Django 5.0.6 on 2024-10-31 11:40

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0015_rename_date_added_post_date_modified_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="post",
            options={"ordering": ("-date_created",)},
        ),
    ]
