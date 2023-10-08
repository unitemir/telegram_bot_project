# Generated by Django 4.2.6 on 2023-10-08 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='timestamp',
            new_name='date_sent',
        ),
        migrations.AddField(
            model_name='customuser',
            name='telegram_token',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
