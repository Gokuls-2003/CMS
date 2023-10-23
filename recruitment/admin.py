from django.contrib import admin
from collections import OrderedDict
from typing import Any
from django.contrib import admin
from django.http.request import HttpRequest
from .import models
from django.contrib.auth.models import User
from staff.models import Staff
# Register your models here.


def approve_applicant(modeladmin, request, queryset):
    for application in queryset:
        if not application.approved:
            user = User.objects.create_user(
                application.email_id,
                application.email_id,
                application.date_of_birth.strftime('%d/%m/%Y'),
                first_name=application.name,
            )
            staff = Staff.objects.create(
                profile_picture=application.profile_picture,
                user=user,
                date_of_birth=application.date_of_birth,
                address=application.address,
                experience=application.experience,
                qualification=application.qualification,
                teaching_type=application.teaching_type,
                department=application.department,
                contact_number=application.contact_number,
                gender=application.gender,
                nationality=application.nationality,
                religion=application.religion
            )
            application.approved = True
            application.save()
    return None


approve_applicant.short_description = "Approve Applications"


# Register your models here.
@admin.register(models.Applicant)
class ApplicantAdmin(admin.ModelAdmin):
    list_filter = ['approved']
    list_display = ["name", "approved"]
    readonly_fields = ["approved"]

    def get_actions(self, request: HttpRequest) -> OrderedDict[Any, Any]:
        actions = super().get_actions(request)
        if request.user.is_superuser:
            actions['approve_applicant'] = (
                approve_applicant, 'approve_applicant', 'Approve selected applicants')
        return actions
