from django.contrib import admin
from . import models
from .import forms

# Register your models here.
# @admin.register(models.Applicant)
# admin.site.register(models.Department)
# admin.site.register(models.Course)
# admin.site.register(models.Classroom)


@admin.register(models.AcademicProgram)
class AcademicProgramAdmin(admin.ModelAdmin):

    form = forms.MyForm


@admin.register(models.Classroom)
class ClassroomAdmin(admin.ModelAdmin):

    form = forms.ClassroomForm


@admin.register(models.Course)
class CourseAdmin(admin.ModelAdmin):

    form = forms.CourseForm


@admin.register(models.Department)
class DeparetmentAdmin(admin.ModelAdmin):

    form = forms.DepartmentForm
