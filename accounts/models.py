from django.db import models
from django.contrib.auth.models import User
from student.models import Student


class Invoice(models.Model):
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name="invoices")
    invoice_number = models.CharField(
        "Invoice Number", max_length=20, unique=True, default=None)
    invoice_name = models.CharField("Invoice Name", max_length=30)
    issue_date = models.DateField("Issue Date")
    due_date = models.DateField("Due Date")
    total_amount = models.FloatField("Total Amount")

    def __str__(self):
        return f"Invoice #{self.invoice_number} - {self.student.user_name.get_full_name()}"


class Transaction(models.Model):
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name="transactions")
    transaction_date = models.DateField()
    description = models.TextField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Transaction - {self.description} - Amount: {self.amount}"


class Expenditure(models.Model):
    description = models.TextField()
    expense_date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Expenditure - {self.description} - Amount: {self.amount}"
