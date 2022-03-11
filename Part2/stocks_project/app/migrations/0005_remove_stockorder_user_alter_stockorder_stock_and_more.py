# Generated by Django 4.0.3 on 2022-03-11 06:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0004_remove_stockorder_investor_stockorder_user_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stockorder',
            name='user',
        ),
        migrations.AlterField(
            model_name='stockorder',
            name='stock',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.stock'),
        ),
        migrations.CreateModel(
            name='Investor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='stockorder',
            name='investor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.investor'),
        ),
    ]
