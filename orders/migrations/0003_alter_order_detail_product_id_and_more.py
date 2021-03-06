# Generated by Django 4.0.2 on 2022-03-11 20:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shipping_detail', '0001_initial'),
        ('product_api', '0006_product_detail_web_heading_and_more'),
        ('orders', '0002_remove_order_detail_states'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order_detail',
            name='product_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_product_info_for_user', to='product_api.product_detail'),
        ),
        migrations.AlterField(
            model_name='order_detail',
            name='shipping_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_shipping_info_of_user', to='shipping_detail.shipping_detail'),
        ),
    ]
