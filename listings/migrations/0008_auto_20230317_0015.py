# Generated by Django 3.2.18 on 2023-03-16 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0007_auto_20230316_0132'),
    ]

    operations = [
        migrations.AddField(
            model_name='ads',
            name='negotiable',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='ads',
            name='price',
            field=models.IntegerField(default=1),
        ),
    ]
