# Generated by Django 5.1.2 on 2025-02-23 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('POST', '0019_alter_postmodel_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='reschedule',
            name='is_approved',
            field=models.BooleanField(default=False),
        ),
    ]
