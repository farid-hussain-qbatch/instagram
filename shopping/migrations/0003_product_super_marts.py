# Generated by Django 3.2.6 on 2021-08-17 11:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0002_auto_20210817_1105'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='super_marts',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shopping.supermart'),
        ),
    ]