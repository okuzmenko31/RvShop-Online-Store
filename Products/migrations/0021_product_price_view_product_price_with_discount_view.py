# Generated by Django 4.1.3 on 2022-12-14 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0020_remove_reviews_user_reviews_ip_reviews_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price_view',
            field=models.CharField(blank=True, default='1', max_length=400, verbose_name='Відредаговане представлення ціни, яке буде бачити користувач'),
        ),
        migrations.AddField(
            model_name='product',
            name='price_with_discount_view',
            field=models.CharField(blank=True, default='1', max_length=400, verbose_name='Відредаговане представлення ціни зі знижкою, яке буде бачити користувач'),
        ),
    ]
