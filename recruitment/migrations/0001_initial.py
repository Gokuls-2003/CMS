# Generated by Django 4.2.6 on 2023-10-24 12:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('department', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Applicant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='profile_pics/')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('email_id', models.EmailField(max_length=100, verbose_name='Email Id')),
                ('date_of_birth', models.DateField()),
                ('address', models.TextField()),
                ('experience', models.CharField(max_length=10, verbose_name='Experience')),
                ('qualification', models.CharField(blank=True, max_length=15, null=True, verbose_name='Qualification')),
                ('teaching_type', models.CharField(choices=[('HOD', 'Hod'), ('P', 'Professor'), ('AP', 'Assistant Professor'), ('LS', 'Lab Staff')], default=None, max_length=3, verbose_name='Teaching Type')),
                ('contact_number', models.CharField(blank=True, max_length=15, null=True, verbose_name='Contact Number')),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=10)),
                ('marital_status', models.CharField(choices=[('Married', 'Married'), ('Un Married', 'Un Married')], max_length=10)),
                ('nationality', models.CharField(max_length=50)),
                ('religion', models.CharField(max_length=50)),
                ('approved', models.BooleanField(default=False)),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='department.department')),
            ],
        ),
    ]
