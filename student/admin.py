from typing import Any
from django.contrib import admin
from django.http.request import HttpRequest
from . import models
from django.db.models import F, ExpressionWrapper, fields, Sum
from .filters import PaidStatus
from django.db.models.query import QuerySet
from django.contrib.auth.models import User


@admin.register(models.Leave)
class Leave(admin.ModelAdmin):

    def get_queryset(self, request: HttpRequest) -> QuerySet:
        queryset = super().get_queryset(request)

        # Check if the user is a student
        if hasattr(request.user, "student"):
            queryset = queryset.filter(student_leave=request.user.student)

        return queryset

    def save_model(self, request, obj, form, change):
        # Set the student_attendance field to the current user if it's not set
        if not obj.student_leave:
            obj.student_leave = request.user.student
        super().save_model(request, obj, form, change)

    def get_readonly_fields(self, request: HttpRequest, obj: Any) -> list[str]:
        if hasattr(request.user, "student"):
            if obj is not None and obj.leave_status != 'P':
                return ['student_leave', 'start_date', 'end_date', 'reason', 'leave_status']
            return ['leave_status']
        if request.user.is_superuser or (hasattr(request.user, "staff") and request.user.staff.teaching_type == "HOD"):
            if obj.leave_status != "P":
                return ['student_leave', 'start_date', 'end_date', 'reason', 'leave_status']
            return ['student_leave', 'start_date', 'end_date', 'reason']
        return []  # safty

    def get_exclude(self, request: HttpRequest, obj: Any) -> list[str]:
        if request.user.is_superuser or (hasattr(request.user, "staff") and request.user.staff.teaching_type == 'HOD'):
            return []
        return ['student_leave']

    def has_add_permission(self, request: HttpRequest) -> bool:
        try:
            if request.user.is_superuser or (hasattr(request.user, "student") and request.user.staff.teaching_type == 'HOD'):
                return False
        except:
            pass
        return super().has_add_permission(request)

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
                Sum('invoices__total_amount') - Sum('transactions__amount'),
                output_field=fields.DecimalField()
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

    def save_model(self, request, obj, form, change):
        # Set the user_name field to the current user if it's not set
        if not obj.user_name:
            obj.user_name = request.user.student.user_name
        super().save_model(request, obj, form, change)


@admin.register(models.Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    def get_queryset(self, request: HttpRequest) -> QuerySet:
        queryset = super().get_queryset(request)

        # Check if the user is a student
        if hasattr(request.user, "student"):
            queryset = queryset.filter(student_attendance=request.user.student)

        return queryset

    def save_model(self, request, obj, form, change):
        # Set the student_attendance field to the current user if it's not set
        if not obj.student_attendance:
            obj.student_attendance = request.user.student
        super().save_model(request, obj, form, change)


@admin.register(models.AcademicRecords)
class AcademicRecordsAdmin(admin.ModelAdmin):
    def get_queryset(self, request: HttpRequest) -> QuerySet:
        queryset = super().get_queryset(request)

        # Check if the user is a student
        if hasattr(request.user, "student"):
            queryset = queryset.filter(student=request.user.student)

        return queryset

    def save_model(self, request, obj, form, change):
        # Set the student_attendance field to the current user if it's not set
        if not obj.student:
            obj.student = request.user.student
        super().save_model(request, obj, form, change)


# admin.site.register(models.Perfromance)

@admin.register(models.Perfromance)
class PeroformanceAdmin(admin.ModelAdmin):
    def get_queryset(self, request: HttpRequest) -> QuerySet:
        queryset = super().get_queryset(request)

        # Check if the user is a student
        if hasattr(request.user, "student"):
            queryset = queryset.filter(student_name=request.user.student)

        return queryset

    def save_model(self, request, obj, form, change):
        # Set the student_attendance field to the current user if it's not set
        if not obj.student_name:
            obj.student_name = request.user.student
        super().save_model(request, obj, form, change)


@admin.register(models.ClassSchedule)
class ClassScheduleAdmin(admin.ModelAdmin):
    list_display = ["course", "class_room",
                    "staff", "day", "start_time", "end_time"]

    def get_queryset(self, request: HttpRequest) -> QuerySet:
        queryset = super().get_queryset(request)

        # Check if the user is a student
        if hasattr(request.user, "student"):
            # Filter schedules based on student's course and academic program
            queryset = queryset.filter(
                course=request.user.student.course, academic_program=request.user.student.academic_program)

        return queryset

    def has_add_permission(self, request: HttpRequest) -> bool:
        # Students should not have permission to add new schedules
        return False

    def has_change_permission(self, request, obj=None) -> bool:
        # Students should not have permission to change existing schedules
        return False

    def has_delete_permission(self, request, obj=None) -> bool:
        # Students should not have permission to delete schedules
        return False
