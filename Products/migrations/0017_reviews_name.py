# Generated by Django 4.1.3 on 2022-12-05 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0016_remove_reviews_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviews',
            name='name',
            field=models.CharField(blank=True, max_length=200, verbose_name="Ім'я користувача"),
        ),
    ]
