# Generated by Django 3.2.18 on 2023-05-16 18:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0043_auto_20230515_2018'),
    ]

    operations = [
        migrations.DeleteModel(
            name='tags',
        ),
        migrations.RemoveField(
            model_name='ads',
            name='no_of_likes',
        ),
    ]
