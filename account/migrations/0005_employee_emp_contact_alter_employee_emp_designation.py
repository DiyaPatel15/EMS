# Generated by Django 5.0.1 on 2024-03-12 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_alter_employee_emp_designation'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='emp_contact',
            field=models.CharField(default=9897969594, max_length=15),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='employee',
            name='emp_designation',
            field=models.CharField(choices=[('CEO', 'CEO'), ('COO', 'COO'), ('Project Manager', 'Project Manager'), ('Jr. PHP Laravel Developer', 'Jr. PHP Laravel Developer'), ('Sr. Developer', 'Sr. Developer'), ('UI/UX Designer', 'UI/UX Designer'), ('Product Manager', 'Product Manager'), ('Quality Engineer', 'Quality Engineer'), ('Quality Engineer Lead', 'Quality Engineer Lead'), ('Web Designer', 'Web Designer'), ('Sr. Developer', 'Sr. Developer'), ('SEO Executive', 'SEO Executive'), ('Jr. HR Executive', 'Jr. HR Executive'), ('Jr. PHP Laravel Developer\t', 'Jr. PHP Laravel Developer'), ('Sr. HR Executive', 'Sr. HR Executive'), ('Sr. SEO Executive', '\tSr. SEO Executive'), ('Content Writer', 'Content Writer'), ('Python Developer', 'Python Developer'), ('Jr. Web Designer', 'Jr. Web Designer'), ('Intern', 'Intern'), ('Lead Generation Executive', 'Lead Generation Executive'), ('Trainee', 'Trainee')], help_text='Employee Designation', max_length=70),
        ),
    ]
