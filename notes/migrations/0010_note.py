# Generated by Django 4.0 on 2022-01-02 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0009_rename_email_id_registration_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.TextField()),
                ('text', models.TextField()),
            ],
        ),
    ]
