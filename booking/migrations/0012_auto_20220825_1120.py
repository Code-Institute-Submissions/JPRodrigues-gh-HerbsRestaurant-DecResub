# Generated by Django 3.2.15 on 2022-08-25 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0011_rename_booking_join_bookingjoin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='confirm',
            field=models.CharField(default='No', max_length=10),
        ),
        migrations.AlterField(
            model_name='booking',
            name='login_email',
            field=models.CharField(max_length=50),
        ),
    ]