# Generated by Django 5.1.2 on 2025-03-01 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('POST', '0026_alter_postman_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='sender_contact',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
