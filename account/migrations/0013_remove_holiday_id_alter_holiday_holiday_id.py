# Generated by Django 5.0.1 on 2024-03-19 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0012_alter_holiday_holiday_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='holiday',
            name='id',
        ),
        migrations.AlterField(
            model_name='holiday',
            name='holiday_id',
            field=models.AutoField(default=None, primary_key=True, serialize=False),
        ),
    ]
