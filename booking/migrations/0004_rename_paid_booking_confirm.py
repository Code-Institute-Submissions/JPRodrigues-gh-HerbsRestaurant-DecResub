# Generated by Django 3.2.15 on 2022-08-11 22:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_auto_20220811_1410'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='paid',
            new_name='confirm',
        ),
    ]
