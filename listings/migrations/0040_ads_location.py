# Generated by Django 3.2.18 on 2023-05-04 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0039_auto_20230501_0029'),
    ]

    operations = [
        migrations.AddField(
            model_name='ads',
            name='location',
            field=models.CharField(choices=[('Raj', 'Rajkot'), ('Morbi', 'Morbi'), ('Jam', 'Jamnagar'), ('Juna', 'Junagadh'), ('GNR', 'Gandhinagar'), ('Bang', 'Bangalore'), ('Bedi', 'Bedi, Rajkot'), ('SM', 'South Mumbai'), ('AM', 'Andheri, Mumbai')], max_length=20, null=True),
        ),
    ]
