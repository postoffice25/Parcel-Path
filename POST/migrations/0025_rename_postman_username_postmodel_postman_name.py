# Generated by Django 5.1.2 on 2025-02-28 00:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('POST', '0024_remove_postman_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postmodel',
            old_name='postman_username',
            new_name='postman_name',
        ),
    ]
