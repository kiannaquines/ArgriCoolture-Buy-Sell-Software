# Generated by Django 4.2.6 on 2023-11-09 14:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_transaction_user_transaction'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='transaction',
            options={'verbose_name': 'Transaction', 'verbose_name_plural': 'Transactions'},
        ),
        migrations.AlterModelTable(
            name='transaction',
            table='transaction_tbl',
        ),
    ]