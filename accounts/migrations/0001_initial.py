# Generated by Django 4.2.6 on 2023-10-11 03:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('student', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expenditure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('expense_date', models.DateField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_date', models.DateField()),
                ('description', models.TextField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='student.student')),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_number', models.CharField(default=None, max_length=20, unique=True, verbose_name='Invoice Number')),
                ('invoice_name', models.CharField(max_length=30, verbose_name='Invoice Name')),
                ('issue_date', models.DateField(verbose_name='Issue Date')),
                ('due_date', models.DateField(verbose_name='Due Date')),
                ('total_amount', models.FloatField(verbose_name='Total Amount')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invoices', to='student.student')),
            ],
        ),
    ]
