# Generated by Django 4.2.4 on 2023-08-28 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_rename_variantproduct_variant_alter_variant_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='variants',
            field=models.ManyToManyField(to='products.variant'),
        ),
    ]
