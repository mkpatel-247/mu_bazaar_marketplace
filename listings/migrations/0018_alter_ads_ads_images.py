# Generated by Django 3.2.18 on 2023-03-18 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0017_alter_ads_ads_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ads',
            name='ads_images',
            field=models.ImageField(default='', upload_to='ads_list/'),
        ),
    ]
