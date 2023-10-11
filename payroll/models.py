from django.db import models
from staff.models import Staff
# Create your models here.


class Salary(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    basic_salary = models.IntegerField("Basic Salary")
    allowances = models.IntegerField("Allowance", default=0)
    deductions = models.IntegerField("Deduction", default=0)
    final_salary = models.IntegerField("Final Salary", default=0)
    generated_at = models.DateTimeField()

    def __str__(self):
        return f"{self.staff.user.get_full_name()}'s Salary"

    class Meta:
        verbose_name = "Salary"
        verbose_name_plural = "Salary"


class Allowance(models.Model):
    salary = models.ForeignKey(
        Salary, on_delete=models.CASCADE, related_name="salary_allowances")
    amount = models.FloatField("Amount")


class Deduction(models.Model):
    salary = models.ForeignKey(
        Salary, on_delete=models.CASCADE, related_name="salary_deductions")
    amount = models.FloatField("Amount")


class Payslip(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    salary = models.ForeignKey(Salary, on_delete=models.CASCADE)
    month = models.DateField("Month")
    generated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payslip for {self.staff.user.get_full_name()} - {self.month}"
