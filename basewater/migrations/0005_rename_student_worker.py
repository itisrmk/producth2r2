# Generated by Django 4.1.5 on 2023-01-14 01:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basewater', '0004_alter_user_is_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Student',
            new_name='Worker',
        ),
    ]