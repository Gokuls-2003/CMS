from .models import Staff, Training
from django import forms
from django.core.exceptions import ValidationError
from email_validator import validate_email, EmailNotValidError
from django.core.files.images import get_image_dimensions
from department.models import Department
from PIL import Image
from datetime import date, timedelta
import re
import datetime


class MyForm(forms.ModelForm):

    class Meta:
        fields = ("profile_picture", 'name',
                  "email_id", "date_of_birth", 'address', 'contact_number', 'qualification', 'teaching_type', 'gender', 'marital_status', 'nationality', 'religion', 'department')
    widgets = {
        'date_of_birth': forms.DateInput(format='%d/%m/%Y', attrs={'placeholder': 'DD/MM/YYYY'}),
    }
    department = forms.ModelChoiceField(
        queryset=Department.objects.all(), empty_label=None)

    def clean_name(self):
        name = self.cleaned_data['name']

        if not name:
            raise ValidationError("Name is required.")

        if not name.replace(' ', '').isalpha():
            raise forms.ValidationError(
                "Name can only contain letters and spaces.")

        # # Check for 5 consecutive characters
        # if any(name[i:i+5].isalpha() for i in range(len(name) - 4)):
        #     raise forms.ValidationError(
        #         "Name cannot have 5 consecutive characters.")

        return name

    def clean_experience(self):
        experience = self.cleaned_data['experience']
        if experience < 2:
            raise forms.ValidationError("Unakku vayasu pathala poo daa")
        if experience > 5:
            raise forms.ValidationError(
                "Unakku romba vayasu aagiruchu poo daa")
        return experience

    def clean_email_id(self):
        email_id = self.cleaned_data.get('email_id')

        try:
            emailinfo = validate_email(email_id, check_deliverability=False)
            email_id = emailinfo.normalized.lower().strip()
        except EmailNotValidError as e:
            raise forms.ValidationError(str(e))

        domain = email_id.split('@')[1]

        if domain not in ['gmail.com', 'yahoo.com']:
            raise forms.ValidationError('Please use your official email id.')

        return email_id

    def clean_profile_picture(self):
        profile_picture = self.cleaned_data.get('profile_picture')
        if profile_picture:
            # Check if the file is an image
            try:
                img = Image.open(profile_picture)
                img.verify()
            except:
                raise ValidationError("Invalid image file.")

            # Check the dimensions of the image
            width, height = get_image_dimensions(profile_picture)
            if width < 100 or height < 100:
                raise ValidationError("Image must be at least 100x100 pixels.")

            # Check the size of the image
            if profile_picture.size > 10*1024*1024:  # 10 MB
                raise ValidationError("Image file size cannot exceed 10 MB.")
        return profile_picture

    def clean_date_of_birth(self):
        date_of_birth = self.cleaned_data.get('date_of_birth')
        if date_of_birth:
            # Get the current date
            current_date = datetime.date.today()

            # Check if the date of birth is in the future
            if date_of_birth > current_date:
                raise ValidationError("Date of birth cannot be in the future.")
        return date_of_birth

    def clean_address(self):
        address = self.cleaned_data.get('address')

        # Split the address into words
        words = address.split()

        # Check the number of words
        if len(words) > 100:
            raise ValidationError("Address cannot have more than 100 words.")

        # Check if there is any 10 consecutive characters in the address
        for word in words:
            if len(word) >= 10:
                raise ValidationError(
                    "Address cannot have 10 consecutive characters.")

        if not address:
            raise ValidationError("Address is required.")

        return address

    def clean_contact_number(self):
        contact_number = self.cleaned_data.get('contact_number')
        if contact_number:
            # Check if the number has exactly 10 digits
            if len(contact_number) != 10:
                raise ValidationError(
                    "contact number must have exactly 10 digits.")

            # Check if the number is an Indian phone number
            if not re.match(r'^[6-9]\d{9}$', contact_number):
                raise ValidationError(
                    "contact number must be an Indian phone number.")

        return contact_number

    def clean_qualification(self):
        qualification = self.cleaned_data.get('qualification')

        if qualification:
            # Check if the qualifications contain only characters, commas, and periods
            if not qualification.replace(' ', '').replace(',', '').replace('.', '').isalpha():
                raise ValidationError(
                    "Qualifications can only contain letters, commas, and periods.")

            # Check if the qualifications contain any numerical values
            if any(char.isdigit() for char in qualification):
                raise ValidationError(
                    "Qualifications cannot contain numerical values.")

            # Check if the qualifications contain no more than 15 characters
            if len(qualification) > 15:
                raise ValidationError(
                    "Qualifications cannot be longer than 15 characters.")

            # Check if the qualifications contain 5 consecutive characters
            # if any(qualification[i:i+5].isalpha() for i in range(len(qualification) - 4)):
            #     raise ValidationError(
            #         "Qualifications cannot have 5 consecutive characters.")

        return qualification

    def clean_teaching_type(self):
        teaching_type = self.cleaned_data.get('teaching_type')
        if not teaching_type:
            raise forms.ValidationError(
                "Teaching Type must be selected.")
        return teaching_type

    def clean_gender(self):
        gender = self.cleaned_data.get('gender')
        if not gender:
            raise forms.ValidationError(
                "Gender must be one of the specified choices.")
        return gender
        # else:
        #     raise forms.ValidationError(
        #         "Gender must be selected.")

    def clean_marital_status(self):
        marital_status = self.cleaned_data.get('marital_status')
        if not marital_status:
            raise forms.ValidationError(
                "Marital Status must be selected.")
        return marital_status

    def clean_nationality(self):
        nationality = self.cleaned_data.get("nationality")
        if not re.match("^[a-zA-Z]*$", nationality):
            raise ValidationError(
                "Nationality can only contain alphabetic characters.")
        if len(nationality) > 35:
            raise ValidationError(
                "Nationality can be at most 35 characters long.")

        # Check if the nationality contains 5 consecutive characters
        # if any(nationality[i:i+5].isalpha() for i in range(len(nationality) - 4)):
        #     raise ValidationError(
        #         "Nationality cannot have 5 consecutive characters.")

        return nationality

    def clean_religion(self):
        religion = self.cleaned_data.get("religion")
        if not re.match("^[a-zA-Z]*$", religion):
            raise ValidationError(
                "Religion can only contain alphabetic characters.")
        if len(religion) > 35:
            raise ValidationError(
                "Religion can be at most 35 characters long.")

        # Check if the religion contains 5 consecutive characters
        # if any(religion[i:i+5].isalpha() for i in range(len(religion) - 4)):
        #     raise ValidationError(
        #         "Religion cannot have 5 consecutive characters.")

        return religion

    def clean_department(self):
        department = self.cleaned_data.get("department")
        if not department:
            raise ValidationError("Department is required.")
        return department


class TrainingForm(forms.ModelForm):

    class Meta:
        model = Training
        fields = ('name', 'staff', 'start_date', 'end_date', 'description')

    def clean_name(self):
        name = self.cleaned_data['name']

        if not name:
            raise ValidationError("Name is required.")

        if not name.replace(' ', '').isalpha():
            raise forms.ValidationError(
                "Name can only contain letters and spaces.")

        # # Check for 5 consecutive characters
        # if any(name[i:i+5].isalpha() for i in range(len(name) - 4)):
        #     raise forms.ValidationError(
        #         "Name cannot have 5 consecutive characters.")

        return name

    def clean_description(self):
        description = self.cleaned_data.get('description')

        # Split the address into words
        words = description.split()

        # Check the number of words
        if len(words) > 100:
            raise ValidationError(
                "description cannot have more than 100 words.")

        # Check if there is any 10 consecutive characters in the address
        for word in words:
            if len(word) >= 10:
                raise ValidationError(
                    "description cannot have 10 consecutive characters.")

        if not description:
            raise ValidationError("Address is required.")

        return description
