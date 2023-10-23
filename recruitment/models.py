from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from department.models import Course, AcademicProgram, Classroom, Department

# Create your models here.


class Applicant(models.Model):
    profile_picture = models.ImageField(
        upload_to='profile_pics/', null=True, blank=True)
    name = models.CharField("Name", max_length=50)
    email_id = models.EmailField("Email Id", max_length=100)
    date_of_birth = models.DateField()
    address = models.TextField()
    experience = models.CharField("Experience", max_length=10)
    qualification = models.CharField(
        "Qualification", max_length=15, blank=True, null=True)
    teaching_type = models.CharField("Teaching Type", max_length=3, default=None, choices=[
        ('HOD', 'Hod'),
        ('P', 'Professor'),
        ('AP', 'Assistant Professor'),
        ('LS', 'Lab Staff')
    ])
    department = models.ForeignKey(
        'department.Department', on_delete=models.CASCADE, blank=True, null=True)
    contact_number = models.CharField(
        'Contact Number', max_length=15,  null=True, blank=True)
    gender = models.CharField(max_length=10, choices=[(
        'Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')])
    marital_status = models.CharField(max_length=10, choices=[(
        'Married', 'Married'), ('Un Married', 'Un Married')])
    nationality = models.CharField(max_length=50)
    religion = models.CharField(max_length=50)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.name
