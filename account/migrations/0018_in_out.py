# Generated by Django 5.0.1 on 2024-03-19 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0017_alter_employee_task_e_mentor_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='In_Out',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('type', models.CharField(choices=[('In', 'In'), ('Out', 'Out')], max_length=50)),
                ('reason', models.CharField(max_length=1000)),
                ('approvel_status', models.CharField(max_length=50)),
            ],
        ),
    ]
