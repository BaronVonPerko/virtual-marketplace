# Generated by Django 5.0.8 on 2024-09-02 06:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("listings", "0005_comment"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Comment",
        ),
    ]
