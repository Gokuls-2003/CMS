from typing import Any
from django.contrib import admin
from django.http.request import HttpRequest
from .import models
# Register your models here.


class AllowanceInline(admin.TabularInline):
    model = models.Allowance
    extra = 0


class DeductionInline(admin.TabularInline):
    model = models.Deduction
    extra = 0


@admin.register(models.Salary)
class SalaryAdmin(admin.ModelAdmin):
    inlines = [AllowanceInline, DeductionInline]
    list_display = ["staff", "generated_at", "basic_salary",
                    "allowances", "deductions", "final_salary"]

    def get_queryset(self, request: HttpRequest):
        queryset = super().get_queryset(request)

        # Check if the user is a student
        if hasattr(request.user, "staff"):
            queryset = queryset.filter(staff=request.user.staff)

        return queryset

    def get_exclude(self, request: HttpRequest, obj: Any | None = ...) -> Any:
        if obj is None:
            return ["allowances", "deductions", "final_salary"]
        return []

    def get_readonly_fields(self, request: HttpRequest, obj: Any | None = ...) -> list[str] | tuple[Any, ...]:
        if obj is not None:
            return ["allowances", "deductions", "final_salary"]
        return []

    def save_formset(self, request: Any, form: Any, formset: Any, change: Any) -> None:
        my_formsets = formset.extra_forms
        if len(my_formsets) > 0:
            obj = my_formsets[0].cleaned_data['salary']
            amount = 0
            for my_formset in my_formsets:
                if not my_formset.cleaned_data['DELETE']:
                    amount += my_formset.cleaned_data["amount"]
            if type(my_formset.instance) == models.Allowance:
                obj.allowances = amount
            if type(my_formset.instance) == models.Deduction:
                obj.deductions = amount
            obj.final_salary = obj.basic_salary+obj.allowances - obj.deductions
            obj.save()
        return super().save_formset(request, form, formset, change)
