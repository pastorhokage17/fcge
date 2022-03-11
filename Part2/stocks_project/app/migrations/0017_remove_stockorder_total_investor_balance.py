# Generated by Django 4.0.3 on 2022-03-11 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_alter_stockorder_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stockorder',
            name='total',
        ),
        migrations.AddField(
            model_name='investor',
            name='balance',
            field=models.PositiveIntegerField(default=10000000),
        ),
    ]
