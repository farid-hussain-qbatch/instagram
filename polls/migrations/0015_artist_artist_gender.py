# Generated by Django 3.2.6 on 2021-08-13 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0014_auto_20210813_0716'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='artist_gender',
            field=models.CharField(choices=[('M', 'Male'), ('F ', 'Female')], max_length=2, null=True),
        ),
    ]
