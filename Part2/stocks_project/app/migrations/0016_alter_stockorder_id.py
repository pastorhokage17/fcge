# Generated by Django 4.0.3 on 2022-03-11 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_stockorder_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockorder',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
