# Generated by Django 3.2.6 on 2021-08-20 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0009_alter_productversion_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productversion',
            name='weight',
            field=models.FloatField(null=True),
        ),
    ]
