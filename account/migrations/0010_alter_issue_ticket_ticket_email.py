# Generated by Django 5.0.1 on 2024-03-18 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_holiday_issue_ticket'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue_ticket',
            name='ticket_email',
            field=models.EmailField(max_length=255, verbose_name='email'),
        ),
    ]
