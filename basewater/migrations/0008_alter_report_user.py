# Generated by Django 4.1.5 on 2023-01-14 05:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basewater', '0007_alter_report_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='basewater.worker'),
        ),
    ]
