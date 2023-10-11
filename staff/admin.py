from typing import Any
from django.contrib import admin
from django.http.request import HttpRequest
from . import models
from .filters import ClassRoomFilter, DayFilter
# Register your models here.


class EmergencyContactInline(admin.TabularInline):
    model = models.EmergencyContact
    extra = 0


class RolesInline(admin.TabularInline):
    model = models.Staff.roles.through
    extra = 0


@admin.register(models.Staff)
class StaffAdmin(admin.ModelAdmin):
    inlines = [EmergencyContactInline, RolesInline]
    fields = ['user', 'contact_information', 'department', 'teaching_type']

    def get_readonly_fields(self, request, obj):
        if obj is None:  # creating
            return []
        return ['user']

    def has_change_permission(self, request, obj=None):

        if request.user.is_superuser or (hasattr(request.user, "staff") and request.user.staff == obj):
            return True
        return False


@admin.register(models.Leave)
class Leave(admin.ModelAdmin):

    def get_readonly_fields(self, request, obj):

        if hasattr(request.user, "staff") and request.user.staff.teaching_type != "HOD":
            if obj is not None and obj.leave_status != "P":
                return ['staff', 'start_date', 'end_date', 'reason', 'leave_status']
        return ['staff', 'start_date', 'end_date', 'reason']

    def get_exclude(self, request, obj):

        if hasattr(request.user, 'staff') and request.user.staff.teaching_type == "HOD":
            return []
        return ['staff']

    def has_add_permission(self, request):

        if hasattr(request.user, 'staff') and request.user.staff.teaching_type == "HOD":
            return False
        return super().has_add_permission(request)

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

    def get_readonly_fields(self, request, obj):

        if hasattr(request.user, "staff") and request.user.staff.teaching_type != "HOD":
            if obj is not None and obj.request_status != "P":
                return ['name', 'staff', 'start_date', 'end_date', 'request_status', 'description']
        return ['name', 'staff', 'start_date', 'end_date', 'description']

    def get_exclude(self, request, obj):

        if hasattr(request.user, 'staff') and request.user.staff.teaching_type == "HOD":
            return []
        return ['staff']

    def has_add_permission(self, request):

        if hasattr(request.user, 'staff') and request.user.staff.teaching_type == "HOD":
            return False
        return super().has_add_permission(request)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.staff = request.user.staff
        return super().save_model(request, obj, form, change)


admin.site.register(models.Role)
admin.site.register(models.PerfromanceEvulation)
admin.site.register(models.Qualification)
admin.site.register(models.Degree)
admin.site.register(models.TeachingType)
