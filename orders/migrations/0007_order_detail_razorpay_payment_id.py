# Generated by Django 4.0.2 on 2022-03-22 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_order_detail_razorpay_order_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order_detail',
            name='razorpay_payment_id',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
