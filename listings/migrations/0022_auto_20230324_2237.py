# Generated by Django 3.2.18 on 2023-03-24 17:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0021_auto_20230324_1658'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ads_images',
            name='ads_name',
        ),
        migrations.AddField(
            model_name='ads_images',
            name='ads_id',
            field=models.ForeignKey(db_column='ads_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='listings.ads'),
        ),
        migrations.AlterField(
            model_name='ads',
            name='category_id',
            field=models.ForeignKey(blank=True, db_column='cat_uid', null=True, on_delete=django.db.models.deletion.CASCADE, to='listings.category'),
        ),
    ]
