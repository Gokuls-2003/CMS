from django import forms
from .models import Salary
from django.core.exceptions import ValidationError
import re


class SalaryForm(forms.ModelForm):

    class Meta:
        model = Salary
        fields = ("basic_salary",)

    def clean_basic_salary(self):
        basic_salary = self.cleaned_data.get('contact_number')
        if basic_salary:
            # Check if the number has exactly 10 digits
            if not basic_salary:
                raise ValidationError(
                    "Basic Salary is required.")

            # Check if the number is an Indian phone number
            if not re.match(r'^[6-9]\d{9}$', basic_salary):
                raise ValidationError(
                    "Basic Salary Must be in Numbers.")

        return basic_salary
