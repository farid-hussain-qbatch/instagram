# Generated by Django 3.2.6 on 2021-08-15 05:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0016_alter_song_album'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='album',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='singer', related_query_name='singers', to='polls.album'),
        ),
    ]
