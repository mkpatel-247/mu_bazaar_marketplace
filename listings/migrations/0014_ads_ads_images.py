# Generated by Django 3.2.18 on 2023-03-18 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0013_auto_20230319_0227'),
    ]

    operations = [
        migrations.AddField(
            model_name='ads',
            name='ads_images',
            field=models.ImageField(default='', upload_to='media/ads_list/'),
        ),
    ]
