# Generated by Django 5.1.2 on 2024-11-05 06:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_product_options_remove_product_price_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='details',
        ),
    ]