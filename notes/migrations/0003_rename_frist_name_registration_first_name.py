# Generated by Django 4.0 on 2021-12-30 18:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_alter_registration_contact_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registration',
            old_name='frist_name',
            new_name='first_name',
        ),
    ]
