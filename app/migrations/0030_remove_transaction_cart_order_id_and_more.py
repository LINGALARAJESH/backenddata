# Generated by Django 5.0.4 on 2024-09-11 06:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0029_remove_transaction_cartorder_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='Cart_order_id',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='user_id',
        ),
    ]
