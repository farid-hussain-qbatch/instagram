# Generated by Django 3.2.6 on 2021-08-12 08:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_auto_20210812_0814'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_plate', models.IntegerField()),
                ('colour', models.CharField(max_length=50)),
                ('car_model', models.CharField(max_length=100)),
                ('seat', models.IntegerField()),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.person')),
            ],
        ),
    ]
