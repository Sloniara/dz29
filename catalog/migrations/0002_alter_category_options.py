# Generated by Django 5.1.7 on 2025-03-13 09:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={"verbose_name": "категория", "verbose_name_plural": "категории"},
        ),
    ]
