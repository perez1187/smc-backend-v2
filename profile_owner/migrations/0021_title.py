# Generated by Django 4.1.1 on 2022-11-11 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_owner', '0020_rename_teachingexperience_profile_owner_teachingexperience'),
    ]

    operations = [
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=32)),
                ('description', models.CharField(blank=True, max_length=32)),
            ],
        ),
    ]
