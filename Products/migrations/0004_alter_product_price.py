# Generated by Django 4.1.3 on 2022-12-01 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0003_product_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(verbose_name='Стоимость товара'),
        ),
    ]
