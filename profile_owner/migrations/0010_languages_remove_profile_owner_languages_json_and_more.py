# Generated by Django 4.1.1 on 2022-09-29 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_owner', '0009_profile_owner_languages_json_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Languages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(blank=True, max_length=32)),
            ],
        ),
        migrations.RemoveField(
            model_name='profile_owner',
            name='languages_json',
        ),
        migrations.AddField(
            model_name='profile_owner',
            name='languages_test',
            field=models.ManyToManyField(blank=True, null=True, to='profile_owner.languages'),
        ),
    ]
