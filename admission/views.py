from django.shortcuts import render
from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import SimpleUploadedFile
from django.conf import settings
from .models import Applicant, ApplicationDocuments
from django.contrib import messages

# Create your views here.


def validate_file_size(value):
    max_size = settings.MAX_UPLOAD_SIZE_MB * 1024*1024
    if value.size > max_size:
        raise ValidationError(
            f"Maximum file size allowed is {settings.MAX_UPLOAD_SIZE_MB} MB.")


def validate_file_format(value):
    allowed_formats = settings.ALLOWED_UPLOAD_FORMATS
    ext = value.name.split('.')[-1].lower()
    if ext not in allowed_formats:
        raise ValidationError(
            f'Invalid file format. Allowed formats: {", ".join(allowed_formats)}.')


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

    uploaded_files = request.FILES.getlist('file')
    for uploaded_file in uploaded_files:
        try:
            validate_file_size(uploaded_file)
            validate_file_format(uploaded_file)
        except ValidationError as e:
            messages.error(request, e.message)
            return render(request, "admission/index.html")

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

    for uploaded_file in uploaded_files:
        ApplicationDocuments.objects.create(
            name=uploaded_file.name,
            document=uploaded_file,
            applicant=applicant
        )

    messages.success(
        request, f"Your Application has Successfully Submitted. #{applicant.pk}")
    return render(request, "admission/index.html")
