# Generated by Django 5.0.6 on 2024-07-13 09:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RealEstate', '0004_rename_tittle_listings_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listings',
            old_name='title',
            new_name='tittle',
        ),
    ]
