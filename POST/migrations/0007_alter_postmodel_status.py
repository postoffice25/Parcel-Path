# Generated by Django 5.1.2 on 2024-12-26 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('POST', '0006_postmodel_postoffice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='status',
            field=models.CharField(choices=[('itempacked', 'item_packed'), ('itemdispatched', 'item_dispatched'), ('itemoutfordelivery', 'item_outfordelivery'), ('itemdelivered', 'item_delivered')], max_length=100),
        ),
    ]
