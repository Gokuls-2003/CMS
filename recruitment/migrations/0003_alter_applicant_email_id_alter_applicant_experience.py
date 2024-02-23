# Generated by Django 4.2.6 on 2024-02-23 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recruitment', '0002_applicant_department_applicant_teaching_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='email_id',
            field=models.EmailField(max_length=100, unique=True, verbose_name='Email Id'),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='experience',
            field=models.IntegerField(max_length=10, verbose_name='Experience'),
        ),
    ]
