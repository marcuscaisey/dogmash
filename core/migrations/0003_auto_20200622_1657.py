# Generated by Django 3.0.7 on 2020-06-22 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_auto_20200622_1645"),
    ]

    operations = [
        migrations.AlterField(
            model_name="dog", name="rating", field=models.DecimalField(decimal_places=3, default=1000, max_digits=7),
        ),
    ]
