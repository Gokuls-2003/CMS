from typing import Any
from django.contrib import admin
from django.http.request import HttpRequest
from . import models
from django.db.models import F, ExpressionWrapper, fields, Sum, Value
from .filters import PaidStatus
from django.db.models.query import QuerySet
from django.contrib.auth.models import User
from django.db.models.functions import Coalesce


@admin.register(models.Leave)
class Leave(admin.ModelAdmin):

    def get_queryset(self, request: HttpRequest) -> QuerySet:
        queryset = super().get_queryset(request)

        # Check if the user is a student
        if hasattr(request.user, "student"):
            queryset = queryset.filter(student_leave=request.user.student)

        return queryset

    def get_readonly_fields(self, request: HttpRequest, obj: Any) -> list[str]:
        if (request.user.is_superuser) or hasattr(request.user, "staff"):
            if obj.leave_status != "P":
                return ['student_leave', 'start_date', 'end_date', 'reason', 'leave_status']
            return ['student_leave', 'start_date', 'end_date', 'reason']
        if hasattr(request.user, "student"):
            if obj is not None and obj.leave_status != 'P':
                return ['student_leave', 'start_date', 'end_date', 'reason', 'leave_status']
            return ['leave_status']
        return []  # safety

    def get_exclude(self, request: HttpRequest, obj: Any) -> list[str]:
        if hasattr(request.user, "staff") and request.user.staff.teaching_type != 'HOD':
            return []
        return ['student_leave']

    def has_add_permission(self, request: HttpRequest) -> bool:
        if super().has_add_permission(request) and hasattr(request.user, "student"):
            return True
        return False

    def save_model(self, request, obj, form, change) -> None:
        if not change and hasattr(request.user, 'student'):
            obj.student_leave = request.user.student
        return super().save_model(request, obj, form, change)


class StudentDocumentInline(admin.TabularInline):
    model = models.StudentDocuments
    extra = 0


@admin.register(models.Student)
class StudentAdmin(admin.ModelAdmin):
    list_filter = [PaidStatus]
    list_display = ["user_name", "get_pending_fees"]
    inlines = [StudentDocumentInline]

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(
            pending_fees=ExpressionWrapper(
                Sum('invoices__total_amount') -
                Coalesce(Sum('transactions__amount'), Value(0.0)),
                output_field=fields.FloatField()
            )

        )

        # Check if the user is a student
        if hasattr(request.user, "student"):
            queryset = queryset.filter(
                user_name=request.user.student.user_name)

        return queryset

    def get_pending_fees(self, obj):
        return obj.pending_fees

    get_pending_fees.short_description = "Pending Fees"
    get_pending_fees.admin_order_field = "pending_fees"


@admin.register(models.Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    def get_queryset(self, request: HttpRequest) -> QuerySet:
        queryset = super().get_queryset(request)

        # Check if the user is a student
        if hasattr(request.user, "student"):
            queryset = queryset.filter(student_attendance=request.user.student)

        return queryset


@admin.register(models.AcademicRecords)
class AcademicRecordsAdmin(admin.ModelAdmin):
    def get_queryset(self, request: HttpRequest) -> QuerySet:
        queryset = super().get_queryset(request)

        # Check if the user is a student
        if hasattr(request.user, "student"):
            queryset = queryset.filter(student=request.user.student)

        return queryset


@admin.register(models.Perfromance)
class PeroformanceAdmin(admin.ModelAdmin):
    def get_queryset(self, request: HttpRequest) -> QuerySet:
        queryset = super().get_queryset(request)

        # Check if the user is a student
        if hasattr(request.user, "student"):
            queryset = queryset.filter(student_name=request.user.student)

        return queryset
