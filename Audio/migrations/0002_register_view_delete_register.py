# Generated by Django 5.1.4 on 2025-02-07 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Audio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='register_view',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('email', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=8)),
                ('cpass', models.CharField(max_length=8)),
            ],
        ),
        migrations.DeleteModel(
            name='register',
        ),
    ]
