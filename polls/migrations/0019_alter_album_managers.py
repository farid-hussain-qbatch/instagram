# Generated by Django 3.2.6 on 2021-08-16 06:41

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0018_auto_20210815_1814'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='album',
            managers=[
                ('albums', django.db.models.manager.Manager()),
            ],
        ),
    ]