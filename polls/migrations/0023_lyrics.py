# Generated by Django 3.2.6 on 2021-08-16 08:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0022_alter_song_album'),
    ]

    operations = [
        migrations.CreateModel(
            name='lyrics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('songs', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='polls.song')),
            ],
        ),
    ]
