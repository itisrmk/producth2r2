# Generated by Django 4.1.5 on 2023-01-14 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basewater', '0003_student_alter_user_options_alter_user_managers_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_user',
            field=models.BooleanField(default=True),
        ),
    ]
