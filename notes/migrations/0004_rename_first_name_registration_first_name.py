# Generated by Django 4.0 on 2021-12-30 18:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0003_rename_frist_name_registration_first_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registration',
            old_name='first_name',
            new_name='First_name',
        ),
    ]
