# Generated by Django 4.1.1 on 2022-09-29 16:43

from django.db import migrations, models
import profile_owner.models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_owner', '0011_uploadimagetest'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile_owner',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to=profile_owner.models.avatar_upload),
        ),
    ]
