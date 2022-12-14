# Generated by Django 3.2.15 on 2022-08-26 12:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('booking_id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_date', models.DateField()),
                ('booking_time', models.TimeField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('last_updated_on', models.DateTimeField(auto_now=True)),
                ('no_of_guests', models.IntegerField()),
                ('confirm', models.CharField(default='No', max_length=10)),
                ('login_email', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ['booking_date'],
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('contact_id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('surname', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=50)),
                ('subject', models.CharField(max_length=50)),
                ('body', models.TextField(max_length=250)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('table_id', models.CharField(max_length=30, unique=True)),
                ('no_of_places', models.IntegerField()),
                ('open', models.IntegerField(choices=[(0, 'Open'), (1, 'Booked')], default=0)),
                ('table_size', models.IntegerField(choices=[(2, '2-Places'), (4, '4-Places'), (6, '6-Places'), (8, '8-Places')])),
            ],
            options={
                'ordering': ['table_id'],
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('surname', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=50)),
                ('login_id', models.CharField(blank=True, max_length=50)),
                ('address1', models.CharField(blank=True, max_length=50)),
                ('address2', models.CharField(blank=True, max_length=50)),
                ('address3', models.CharField(blank=True, max_length=50)),
                ('postal_code', models.CharField(blank=True, max_length=50)),
                ('town_city', models.CharField(blank=True, max_length=50)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='BookingJoin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.booking')),
                ('table_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.table')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.user')),
            ],
        ),
    ]
