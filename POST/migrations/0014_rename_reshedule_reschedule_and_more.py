# Generated by Django 5.1.2 on 2025-01-25 09:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('POST', '0013_reshedule'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='reshedule',
            new_name='reschedule',
        ),
        migrations.RenameField(
            model_name='reschedule',
            old_name='resheduled_date',
            new_name='rescheduled_date',
        ),
    ]
