# Generated by Django 4.1.6 on 2023-02-17 10:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emotion_detect', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='records_log',
            old_name='emotion',
            new_name='Emotion',
        ),
        migrations.RenameField(
            model_name='records_log',
            old_name='time',
            new_name='Time',
        ),
    ]
