# Generated by Django 4.1.5 on 2023-01-14 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basewater', '0006_report'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='link',
            field=models.URLField(default=None),
        ),
    ]
