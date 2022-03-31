# Generated by Django 4.0.2 on 2022-03-04 09:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product_Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_images', models.ImageField(blank=True, null=True, upload_to='uploads/')),
                ('alt', models.CharField(blank=True, max_length=20, null=True)),
                ('prdouct_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prdouct_image', to='product_api.product_detail')),
            ],
        ),
    ]