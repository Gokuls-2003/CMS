from typing import Any
from django.contrib import admin
from django.http.request import HttpRequest
from . import models
from .filters import ClassRoomFilter, DayFilter
from django.db.models.query import QuerySet
# Register your models here.


class EmergencyContactInline(admin.TabularInline):
    model = models.EmergencyContact
    extra = 0


# class RolesInline(admin.TabularInline):
#     model = models.Staff.roles.through
#     extra = 0


@admin.register(models.Staff)
class StaffAdmin(admin.ModelAdmin):
    inlines = [EmergencyContactInline]
    fields = ['user', 'contact_information', 'department', 'teaching_type',
              'date_of_birth', 'gender', 'marital_status', 'nationality', 'religion', 'address']

    def get_readonly_fields(self, request, obj):
        if obj is None:  # creating
            return []
        return ['user']

    def get_queryset(self, request: HttpRequest) -> QuerySet:
        queryset = super().get_queryset(request)

        # Check if the user is a student
        if hasattr(request.user, "staff"):
            queryset = queryset.filter(user=request.user)

        return queryset


@admin.register(models.Leave)
class Leave(admin.ModelAdmin):

    def get_queryset(self, request: HttpRequest) -> QuerySet:
        queryset = super().get_queryset(request)

        # Check if the user is a student
        if hasattr(request.user, "staff") and request.user.staff.teaching_type != "HOD":
            queryset = queryset.filter(staff=request.user.staff)

        return queryset

    # def get_readonly_fields(self, request, obj):
    #     if hasattr(request.user, "staff") and request.user.staff.teaching_type != "HOD":
    #         if obj is not None and obj.leave_status != "P":
    #             return ['staff', 'start_date', 'end_date', 'reason', 'leave_status']
    #         return ['leave_status']
    #     if obj.leave_status != "P":
    #         return ['staff', 'start_date', 'end_date', 'reason', 'leave_status']
    #     return ['staff', 'start_date', 'end_date', 'reason']

    def get_readonly_fields(self, request: HttpRequest, obj: Any) -> list[str]:
        if request.user.is_superuser or (hasattr(request.user, "staff") and request.user.staff.teaching_type == "HOD"):
            if obj.leave_status != "P":
                return ['staff', 'start_date', 'end_date', 'reason', 'leave_status']
            return ['staff', 'start_date', 'end_date', 'reason']
        if hasattr(request.user, "staff"):
            if obj is not None and obj.leave_status != 'P':
                return ['staff', 'start_date', 'end_date', 'reason', 'leave_status']
            return ['leave_status']
        return []  # safety

    def get_exclude(self, request, obj):

        if hasattr(request.user, 'staff') and request.user.staff.teaching_type != "HOD":
            return ['staff']
        return []

    def has_add_permission(self, request):
        if super().has_add_permission(request):
            if hasattr(request.user, 'staff') and request.user.staff.teaching_type != "HOD":
                return True
        return False

    def save_model(self, request, obj, form, change):
        if not change:
            obj.staff = request.user.staff
        return super().save_model(request, obj, form, change)


@admin.register(models.ClassSchecule)
class ClassScheduleAdmin(admin.ModelAdmin):
    list_filter = [ClassRoomFilter, DayFilter]


# admin.site.register(models.Training)


@admin.register(models.Training)
class TrainingAdmin(admin.ModelAdmin):

    def get_queryset(self, request: HttpRequest) -> QuerySet:
        queryset = super().get_queryset(request)

        # Check if the user is a student
        if hasattr(request.user, "staff") and request.user.staff.teaching_type != "HOD":
            queryset = queryset.filter(staff=request.user.staff)

        return queryset

    # def get_readonly_fields(self, request, obj):

    #     if hasattr(request.user, "staff") and request.user.staff.teaching_type != "HOD":
    #         if obj is not None and obj.request_status != "P":
    #             return ['name', 'staff', 'start_date', 'end_date', 'request_status', 'description']
    #     return ['request_status']

    def get_readonly_fields(self, request: HttpRequest, obj: Any) -> list[str]:
        if request.user.is_superuser or (hasattr(request.user, "staff") and request.user.staff.teaching_type == "HOD"):
            if obj.request_status != "P":
                return ['name', 'staff', 'start_date', 'end_date', 'request_status', 'description']
            return ['name', 'staff', 'start_date', 'end_date', 'description']
        if hasattr(request.user, "staff"):
            if obj is not None and obj.request_status != 'P':
                return ['name', 'staff', 'start_date', 'end_date', 'request_status', 'description']
            return ['request_status']
        return []  # safety

    def get_exclude(self, request, obj):

        if hasattr(request.user, 'staff') and request.user.staff.teaching_type != "HOD":
            return ['staff']
        return []

    def has_add_permission(self, request):
        if super().has_add_permission(request):
            if hasattr(request.user, 'staff') and request.user.staff.teaching_type != "HOD":
                return True
        return False

    def save_model(self, request, obj, form, change):
        if not change:
            obj.staff = request.user.staff
        return super().save_model(request, obj, form, change)


# admin.site.register(models.PerfromanceEvulation)


@admin.register(models.PerfromanceEvulation)
class PeroformanceEvulationAdmin(admin.ModelAdmin):
    def get_queryset(self, request: HttpRequest) -> QuerySet:
        queryset = super().get_queryset(request)

        # Check if the user is a staff
        if hasattr(request.user, "staff"):
            queryset = queryset.filter(staff=request.user.staff)

        return queryset


# admin.site.register(models.Role)


# admin.site.register(models.Qualification)
@admin.register(models.Qualification)
class QualificationAdmin(admin.ModelAdmin):
    def get_queryset(self, request: HttpRequest) -> QuerySet:
        queryset = super().get_queryset(request)

        # Check if the user is a staff
        if hasattr(request.user, "staff"):
            queryset = queryset.filter(staff=request.user.staff)

        return queryset


admin.site.register(models.Degree)
