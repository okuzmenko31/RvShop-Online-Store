# Generated by Django 4.1.3 on 2022-12-03 20:57

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Order', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'замовлення', 'verbose_name_plural': 'Замовлення'},
        ),
        migrations.AlterField(
            model_name='order',
            name='confirm_call',
            field=models.BooleanField(default=False, verbose_name='Дзвінок для підтвердження'),
        ),
        migrations.AlterField(
            model_name='order',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='Замовлення підтверджено'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_total_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20, verbose_name='Вартість товару'),
        ),
        migrations.AlterField(
            model_name='order',
            name='patronymic',
            field=models.CharField(max_length=300, verbose_name='По-батькові замовник'),
        ),
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=models.CharField(blank=True, max_length=200, verbose_name='Номер телефону замовника'),
        ),
        migrations.AlterField(
            model_name='order',
            name='products_amount',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)], verbose_name='Кількість товарів в замовленні'),
        ),
        migrations.AlterField(
            model_name='order',
            name='real_name',
            field=models.CharField(max_length=300, verbose_name="Ім'я замовник"),
        ),
        migrations.AlterField(
            model_name='order',
            name='surname',
            field=models.CharField(max_length=300, verbose_name='Фамілія замовник'),
        ),
        migrations.AlterField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL, verbose_name='Замовник'),
        ),
    ]
