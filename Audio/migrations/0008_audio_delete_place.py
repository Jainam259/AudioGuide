# Generated by Django 5.1.6 on 2025-03-03 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Audio', '0007_place'),
    ]

    operations = [
        migrations.CreateModel(
            name='audio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_path_english', models.FileField(blank=True, null=True, upload_to='files')),
            ],
        ),
        migrations.DeleteModel(
            name='Place',
        ),
    ]
