# Generated by Django 4.2.6 on 2023-10-23 17:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0007_rename_contact_numbrer_staff_contact_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staff',
            name='department',
        ),
    ]