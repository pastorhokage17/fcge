# Generated by Django 4.0.3 on 2022-03-11 08:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_remove_stockorder_user_alter_stockorder_stock_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='investor',
            old_name='user',
            new_name='name',
        ),
    ]