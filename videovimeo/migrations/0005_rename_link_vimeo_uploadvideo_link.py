# Generated by Django 4.1.1 on 2022-10-03 16:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videovimeo', '0004_rename_link_lokal_uploadvideo_link_vimeo_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='uploadvideo',
            old_name='link_vimeo',
            new_name='link',
        ),
    ]
