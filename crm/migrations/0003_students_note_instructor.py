# Generated by Django 4.1.1 on 2022-10-04 13:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profile_owner', '0014_profile_owner_is_instructor'),
        ('crm', '0002_alter_student_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='students_note',
            name='instructor',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='profile_owner.profile_owner'),
        ),
    ]
