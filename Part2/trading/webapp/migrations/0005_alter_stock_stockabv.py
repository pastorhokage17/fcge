# Generated by Django 4.0.3 on 2022-03-10 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_stock_stockprice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='stockAbv',
            field=models.CharField(default='$', max_length=5),
        ),
    ]