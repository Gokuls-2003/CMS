from django.shortcuts import render
from .models import Applicant
from django.contrib import messages

# Create your views here.


def student_application(request):
    if request.method == "GET":
        return render(request, "admission/index.html")
    profile_picture = request.FILES.get('profile_picture')
    name = request.POST.get('name')
    email_id = request.POST.get('email_id')
    date_of_birth = request.POST.get('date_of_birth')
    address = request.POST.get('address')
    tenth_mark = request.POST.get('tenth_mark')
    twelveth_mark = request.POST.get('twelveth_mark')
    contact_number = request.POST.get('contact_number')
    emergency_contact_name = request.POST.get('emergency_contact_name')
    emergency_contact_number = request.POST.get('emergency_contact_number')
    gender = request.POST.get('gender')
    nationality = request.POST.get('nationality')
    religion = request.POST.get('religion')

    applicant = Applicant.objects.create(
        profile_picture=profile_picture,
        name=name,
        email_id=email_id,
        date_of_birth=date_of_birth,
        address=address,
        tenth_mark=tenth_mark,
        twelveth_mark=twelveth_mark,
        contact_number=contact_number,
        emergency_contact_name=emergency_contact_name,
        emergency_contact_number=emergency_contact_number,
        gender=gender,
        nationality=nationality,
        religion=religion
    )
    messages.success(
        request, f"Your Application has Successfully Submitted. #{applicant.pk}")
    return render(request, "admission/index.html")
