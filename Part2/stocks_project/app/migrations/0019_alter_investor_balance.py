# Generated by Django 4.0.3 on 2022-03-11 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_alter_investor_total_stock_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investor',
            name='balance',
            field=models.PositiveIntegerField(default=50000, editable=False),
        ),
    ]
