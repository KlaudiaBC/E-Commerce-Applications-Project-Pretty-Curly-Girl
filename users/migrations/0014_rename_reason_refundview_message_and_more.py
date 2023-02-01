# Generated by Django 4.0 on 2023-02-01 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_refundview'),
    ]

    operations = [
        migrations.RenameField(
            model_name='refundview',
            old_name='reason',
            new_name='message',
        ),
        migrations.RemoveField(
            model_name='refundview',
            name='order',
        ),
        migrations.AddField(
            model_name='refundview',
            name='reference',
            field=models.CharField(default='abc', max_length=50),
        ),
    ]
