# Generated by Django 3.2.6 on 2021-08-17 06:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0029_alter_lyrics_songs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lyrics',
            name='songs',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='polls.song'),
        ),
    ]