# Generated by Django 3.0.7 on 2020-06-22 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.DecimalField(decimal_places=3, max_digits=7)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]
