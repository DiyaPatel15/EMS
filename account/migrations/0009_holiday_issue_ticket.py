# Generated by Django 5.0.1 on 2024-03-18 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_alter_employee_emp_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Holiday',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('holiday_date', models.DateField()),
                ('holiday_name', models.CharField(help_text='Employee Name', max_length=50)),
                ('holiday_day', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Issue_Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket_email', models.EmailField(max_length=255, unique=True, verbose_name='email')),
                ('ticket_issue', models.TextField()),
            ],
        ),
    ]