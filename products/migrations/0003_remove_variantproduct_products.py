# Generated by Django 4.2.4 on 2023-08-28 12:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_product_options_alter_product_unit_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='variantproduct',
            name='products',
        ),
    ]
