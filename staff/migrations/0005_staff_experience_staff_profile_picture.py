# Generated by Django 4.2.6 on 2023-10-23 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0004_staff_address_staff_date_of_birth'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='experience',
            field=models.CharField(default=0, max_length=10, verbose_name='Experience'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='staff',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pics/'),
        ),
    ]
