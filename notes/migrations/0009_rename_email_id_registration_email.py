# Generated by Django 3.2.9 on 2021-12-31 17:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0008_rename_contact_number_registration_mobile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registration',
            old_name='email_id',
            new_name='email',
        ),
    ]