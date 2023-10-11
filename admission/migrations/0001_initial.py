# Generated by Django 4.2.6 on 2023-10-11 03:50

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Applicant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='profile_pics/')),
                ('name', models.CharField(max_length=50, verbose_name='Student Name')),
                ('email_id', models.EmailField(max_length=100, verbose_name='Email Id')),
                ('date_of_birth', models.DateField()),
                ('address', models.TextField()),
                ('tenth_mark', models.IntegerField(validators=[django.core.validators.MinValueValidator(175), django.core.validators.MaxValueValidator(500)], verbose_name='10th')),
                ('twelveth_mark', models.IntegerField(validators=[django.core.validators.MinValueValidator(270), django.core.validators.MaxValueValidator(600)], verbose_name='12th')),
                ('contact_number', models.CharField(max_length=15)),
                ('emergency_contact_name', models.CharField(max_length=30)),
                ('emergency_contact_number', models.CharField(max_length=15)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=10)),
                ('nationality', models.CharField(max_length=50)),
                ('religion', models.CharField(max_length=50)),
                ('approved', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ApplicationDocuments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Document Name')),
                ('document', models.FileField(upload_to='application_documents/', verbose_name='Document')),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='documents', to='admission.applicant')),
            ],
        ),
    ]
