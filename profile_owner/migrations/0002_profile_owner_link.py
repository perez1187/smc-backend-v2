# Generated by Django 4.1.1 on 2022-09-27 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_owner', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile_owner',
            name='link',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
