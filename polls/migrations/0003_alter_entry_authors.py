# Generated by Django 3.2.6 on 2021-08-12 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20210812_0536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='authors',
            field=models.ManyToManyField(related_name='auth', to='polls.Author'),
        ),
    ]