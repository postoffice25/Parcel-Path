# Generated by Django 5.1.2 on 2025-02-27 23:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('POST', '0023_reschedule_razorpay_order_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postman',
            name='username',
        ),
    ]
