# Generated by Django 4.0.3 on 2022-03-11 06:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0003_stockorder_investor_alter_stockorder_quantity_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stockorder',
            name='investor',
        ),
        migrations.AddField(
            model_name='stockorder',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Investor',
        ),
    ]
