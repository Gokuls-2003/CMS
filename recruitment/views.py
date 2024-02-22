from django.shortcuts import render
from .models import Applicant
from django.contrib import messages
from .forms import MyForm

# Create your views here.


def my_view(request):
    if request.method == 'POST':
        form = MyForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the form data
            # def staff_recruiment(request):
            # if request.method == "GET":
            #     return render(request, "recruitment/index.html")
            profile_picture = request.FILES.get('profile_picture')
            name = request.POST.get('name')
            email_id = request.POST.get('email_id')
            date_of_birth = request.POST.get('date_of_birth')
            address = request.POST.get('address')
            experience = request.POST.get('experience')
            qualification = request.POST.get('Qualifications')
            contact_number = request.POST.get('contact_number')
            emergency_contact_name = request.POST.get('emergency_contact_name')
            emergency_contact_number = request.POST.get(
                'emergency_contact_number')
            gender = request.POST.get('gender')
            nationality = request.POST.get('nationality')
            religion = request.POST.get('religion')
            try:
                Applicant.objects.get(email_id=email_id)
                messages.info(
                    request, f"Application already Submitted.")
            except Applicant.DoesNotExist:
                applicant = Applicant.objects.create(
                    profile_picture=profile_picture,
                    name=name,
                    email_id=email_id,
                    date_of_birth=date_of_birth,
                    address=address,
                    experience=experience,
                    qualification=qualification,
                    contact_number=contact_number,
                    emergency_contact_name=emergency_contact_name,
                    emergency_contact_number=emergency_contact_number,
                    gender=gender,
                    nationality=nationality,
                    religion=religion
                )
                messages.info(
                    request, f"Your Application has Successfully Submitted. #{applicant.pk}")
            return render(request, "recruitment/index.html")

            form.save()
            messages.info(
                request, f"Your Application has Successfully Submitted.")
            return render(request, 'recruitment/index.html', {'form': form})
    else:
        form = MyForm()
    return render(request, 'recruitment/index.html', {'form': form})


# def staff_recruiment(request):
#     if request.method == "GET":
#         return render(request, "recruitment/index.html")
#         profile_picture = request.FILES.get('profile_picture')
#         name = request.POST.get('name')
#         email_id = request.POST.get('email_id')
#         date_of_birth = request.POST.get('date_of_birth')
#         address = request.POST.get('address')
#         experience = request.POST.get('experience')
#         qualification = request.POST.get('Qualifications')
#         contact_number = request.POST.get('contact_number')
#         # emergency_contact_name = request.POST.get('emergency_contact_name')
#         # emergency_contact_number = request.POST.get('emergency_contact_number')
#         gender = request.POST.get('gender')
#         nationality = request.POST.get('nationality')
#         religion = request.POST.get('religion')
#         try:
#             Applicant.objects.get(email_id=email_id)
#             messages.info(
#                 request, f"Application already Submitted.")
#         except Applicant.DoesNotExist:
#             applicant = Applicant.objects.create(
#                 profile_picture=profile_picture,
#                 name=name,
#                 email_id=email_id,
#                 date_of_birth=date_of_birth,
#                 address=address,
#                 experience=experience,
#                 qualification=qualification,
#                 contact_number=contact_number,
#                 # emergency_contact_name=emergency_contact_name,
#                 # emergency_contact_number=emergency_contact_number,
#                 gender=gender,
#                 nationality=nationality,
#                 religion=religion
#             )
#             messages.info(
#                 request, f"Your Application has Successfully Submitted. #{applicant.pk}")
#         return render(request, "recruitment/index.html")
