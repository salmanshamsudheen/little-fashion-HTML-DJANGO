# Generated by Django 5.1.3 on 2024-11-29 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_created_date_product_is_popular'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
