# Generated by Django 3.2.16 on 2022-11-20 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_rename_birthday_userprofile_birthdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.PositiveSmallIntegerField(blank=True, choices=[('GENDER_MALE', 'Male'), ('GENDER_FEMALE', 'Female'), ('GENDER_OTHER', 'Other')], null=True),
        ),
    ]
