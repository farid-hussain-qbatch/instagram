# Generated by Django 3.2.6 on 2021-08-12 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_subject_person'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='number_plate',
            field=models.CharField(max_length=50),
        ),
    ]
