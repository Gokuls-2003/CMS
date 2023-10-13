from django.contrib import admin
from . import models

# Register your models here.


# admin.site.register(models.Invoice)
@admin.register(models.Transaction)
class TransactionAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        queryset = super().get_queryset(request)

        # Check if the user is a student
        if hasattr(request.user, "student"):
            queryset = queryset.filter(student=request.user.student)

        return queryset


# admin.site.register(models.Transaction)
@admin.register(models.Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        queryset = super().get_queryset(request)

        # Check if the user is a student
        if hasattr(request.user, "student"):
            queryset = queryset.filter(student=request.user.student)

        return queryset


admin.site.register(models.Expenditure)
