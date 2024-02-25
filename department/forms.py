from django import forms
from .models import AcademicProgram, Department, Classroom, Course
from django.core.exceptions import ValidationError


class MyForm(forms.ModelForm):

    class Meta:
        model = AcademicProgram
        fields = ("name", 'code')

    def clean_name(self):
        name = self.cleaned_data["name"]
        if not name:
            raise ValidationError("Program is required.")

        if not name.replace(' ', '').isalpha():
            raise forms.ValidationError(
                "Program can only contain letters and spaces.")

        # for character in name:
        #     if len(character) >= 4:
        #         raise ValidationError(
        #             "Name cannot have 4 consecutive characters.")

        # # Check for 5 consecutive characters
        # if any(name[i:i+5].isalpha() for i in range(len(name) - 4)):
        #     raise forms.ValidationError(
        #         "Name cannot have 5 consecutive characters.")

        return name

    def clean_code(self):
        code = self.cleaned_data['code']

        if not code:
            raise ValidationError("Code is required")

        if not code.isalnum():
            raise ValidationError(
                'Code must contain only alphanumeric characters.')

        return code


class ClassroomForm(forms.ModelForm):

    class Meta:
        model = Classroom
        fields = ('name',)

    def clean_name(self):
        name = self.cleaned_data['name']

        if not name:
            raise ValidationError("Classroom is required")

        if not name.isalnum():
            raise ValidationError(
                'Classroom must contain only alphanumeric characters.')

        return name


class CourseForm(forms.ModelForm):

    class Meta:
        model = Course
        fields = ('name', 'code', 'description', 'program')

    def clean_name(self):
        name = self.cleaned_data["name"]
        if not name:
            raise ValidationError("Course Name is required.")

        if not name.replace(' ', '').isalpha():
            raise forms.ValidationError(
                "Course Name can only contain letters and spaces.")

        # # Check for 5 consecutive characters
        # if any(name[i:i+5].isalpha() for i in range(len(name) - 4)):
        #     raise forms.ValidationError(
        #         "Name cannot have 5 consecutive characters.")

        return name

    def clean_code(self):
        code = self.cleaned_data['code']

        if not code:
            raise ValidationError("Code is required")

        if not code.isalnum():
            raise ValidationError(
                'Code must contain only alphanumeric characters.')

        return code

    def clean_description(self):
        description = self.cleaned_data['description']

        if not description:
            raise ValidationError("description is required")

        words = description.split()

        # Check the number of words
        if len(words) > 100:
            raise ValidationError(
                "description cannot have more than 100 words.")

        # Check if there is any 10 consecutive characters in the address
        for word in words:
            if len(word) >= 3:
                raise ValidationError(
                    "description only contains minimum 3 consecutive characters.")

        return description


class DepartmentForm(forms.ModelForm):

    class Meta:
        model = Department
        fields = ('department_name',)

    def clean_department_name(self):
        department_name = self.cleaned_data["department_name"]
        if not department_name:
            raise ValidationError("Department Name is required.")

        if not department_name.replace(' ', '').isalpha():
            raise forms.ValidationError(
                "Department Name can only contain letters and spaces.")

        return department_name
