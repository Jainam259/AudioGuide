# Generated by Django 5.1.6 on 2025-03-15 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Audio', '0015_delete_booking_remove_monument_photos_monument_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('card_name', models.CharField(max_length=255)),
                ('card_number', models.CharField(max_length=16)),
                ('exp_month', models.CharField(max_length=20)),
                ('exp_year', models.CharField(max_length=4)),
                ('cvv', models.CharField(max_length=4)),
                ('charges', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
