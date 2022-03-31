# Generated by Django 4.0.2 on 2022-03-05 01:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product_api', '0004_alter_product_detail_product_about'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product_how_to_use',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('how_to_use', models.CharField(blank=True, max_length=200, null=True)),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prdouct_how_to_use', to='product_api.product_detail')),
            ],
        ),
    ]