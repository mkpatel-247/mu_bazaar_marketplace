# Generated by Django 3.2.18 on 2023-03-16 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0009_auto_20230317_0017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_slug',
            field=models.SlugField(max_length=30),
        ),
    ]
