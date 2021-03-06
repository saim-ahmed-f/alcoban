# Generated by Django 4.0.2 on 2022-03-04 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_api', '0002_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_detail',
            name='delivery_charge',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product_detail',
            name='discount_value',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product_detail',
            name='product_online_price',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
