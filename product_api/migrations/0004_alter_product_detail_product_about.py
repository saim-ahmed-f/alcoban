# Generated by Django 4.0.2 on 2022-03-04 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_api', '0003_product_detail_delivery_charge_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_detail',
            name='product_about',
            field=models.TextField(blank=True, null=True),
        ),
    ]
