# Generated by Django 5.1.5 on 2025-01-17 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0002_message_subject'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='is_sent',
        ),
        migrations.AlterField(
            model_name='deliverylog',
            name='status',
            field=models.CharField(choices=[('sent', 'Sent'), ('failed', 'Failed')], max_length=20),
        ),
    ]