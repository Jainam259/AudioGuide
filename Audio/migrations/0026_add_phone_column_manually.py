from django.db import migrations, models

class Migration(migrations.Migration):
    dependencies = [
        ('Audio', '0025_rename_mobile_booking_phone_number'),
    ]

    operations = [
        migrations.RunSQL(
            sql="ALTER TABLE Audio_booking ADD COLUMN phone_number varchar(15);",
            reverse_sql="", # Empty reverse SQL to prevent errors
        )
    ] 