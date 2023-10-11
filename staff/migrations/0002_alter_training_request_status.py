# Generated by Django 4.2.6 on 2023-10-11 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='training',
            name='request_status',
            field=models.CharField(choices=[('P', 'Pending'), ('A', 'Approved'), ('D', 'Denied')], default='P', max_length=1, verbose_name='Request Status'),
        ),
    ]