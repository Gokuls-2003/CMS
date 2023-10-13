from collections import OrderedDict
from typing import Any
from django.contrib import admin
from django.http.request import HttpRequest
from .import models
from django.contrib.auth.models import User
from student.models import Student, StudentDocuments
from .filters import TenthMarkFilter, TwelvethMarkFilter
# Register your models here.


def approve_applicant(modeladmin, request, queryset):
    for application in queryset:
        if not application.approved:
            user = User.objects.create_user(
                application.email_id,
                application.email_id,
                application.date_of_birth.strftime('%d/%m/%Y'),
                first_name=application.name,
                is_staff=True
            )
            student = Student.objects.create(
                profile_picture=application.profile_picture,
                user_name=user,
                date_of_birth=application.date_of_birth,
                address=application.address,
                tenth_mark=application.tenth_mark,
                twelveth_mark=application.twelveth_mark,
                contact_number=application.contact_number,
                emergency_contact_name=application.emergency_contact_name,
                emergency_contact_number=application.emergency_contact_number,
                gender=application.gender,
                nationality=application.nationality,
                religion=application.religion
            )
            for document in application.documents.all():
                StudentDocuments.objects.create(
                    name=document.name,
                    document=document.document,
                    student=student
                )
            application.approved = True
            application.save()
    return None


approve_applicant.short_description = "Approve Applications"


class ApplicantDocumentInline(admin.TabularInline):
    model = models.ApplicationDocuments
    extra = 0


@admin.register(models.Applicant)
class ApplicantAdmin(admin.ModelAdmin):
    list_filter = ["approved", TenthMarkFilter, TwelvethMarkFilter]
    list_display = ["name", "approved", "tenth_mark", "twelveth_mark"]
    readonly_fields = ["approved"]
    inlines = [ApplicantDocumentInline]

    def get_actions(self, request: HttpRequest) -> OrderedDict[Any, Any]:
        actions = super().get_actions(request)
        if request.user.is_superuser:
            actions['approve_applicant'] = (
                approve_applicant, 'approve_applicant', 'Approve selected applicants')
        return actions
