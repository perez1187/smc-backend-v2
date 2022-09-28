# Generated by Django 4.1.1 on 2022-09-28 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_chess_instructor_profile_chess_actual_rating_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='chess_instructor_profile',
            name='accepts_new_students',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='chess_instructor_profile',
            name='chess_com',
            field=models.URLField(default=''),
        ),
        migrations.AddField(
            model_name='chess_instructor_profile',
            name='facebook',
            field=models.URLField(default=''),
        ),
        migrations.AddField(
            model_name='chess_instructor_profile',
            name='hidden_message',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='chess_instructor_profile',
            name='instagram',
            field=models.URLField(default=''),
        ),
        migrations.AddField(
            model_name='chess_instructor_profile',
            name='languages',
            field=models.CharField(blank=True, default='eng', max_length=16),
        ),
        migrations.AddField(
            model_name='chess_instructor_profile',
            name='lichess',
            field=models.URLField(default=''),
        ),
        migrations.AddField(
            model_name='chess_instructor_profile',
            name='profile_is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='chess_instructor_profile',
            name='tiktok',
            field=models.URLField(default=''),
        ),
        migrations.AddField(
            model_name='chess_instructor_profile',
            name='twitter',
            field=models.URLField(default=''),
        ),
        migrations.AddField(
            model_name='chess_instructor_profile',
            name='youtube',
            field=models.URLField(default=''),
        ),
    ]
