# Generated by Django 5.1.6 on 2025-03-04 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Audio', '0011_audio'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='city_images/')),
                ('rating', models.FloatField(default=0)),
                ('reviews', models.IntegerField(default=0)),
                ('opening_time', models.TimeField()),
                ('closing_time', models.TimeField()),
                ('days_open', models.CharField(max_length=255)),
                ('contact_number', models.CharField(max_length=20)),
            ],
        ),
    ]
