# Generated by Django 4.1.3 on 2022-12-02 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0007_alter_productcategory_subcategory'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['-id'], 'verbose_name': 'товар', 'verbose_name_plural': 'Товары'},
        ),
        migrations.AlterModelOptions(
            name='productcategory',
            options={'ordering': ['id'], 'verbose_name': 'категория товаров', 'verbose_name_plural': 'Категории товаров'},
        ),
        migrations.AlterField(
            model_name='product',
            name='discount',
            field=models.IntegerField(verbose_name='Скидка на товар'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price_with_discount',
            field=models.IntegerField(verbose_name='стоимость товара со скидкой'),
        ),
    ]
