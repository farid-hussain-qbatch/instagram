# Generated by Django 3.2.6 on 2021-08-16 06:53

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0019_alter_album_managers'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='album',
            managers=[
            ],
        ),
        migrations.AlterModelManagers(
            name='song',
            managers=[
                ('songs', django.db.models.manager.Manager()),
            ],
        ),
    ]
