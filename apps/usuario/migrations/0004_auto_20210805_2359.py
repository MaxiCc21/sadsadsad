# Generated by Django 2.2.13 on 2021-08-06 02:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0004_auto_20210805_2357'),
        ('usuario', '0003_auto_20210805_2357'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Usuario',
            new_name='User',
        ),
    ]
