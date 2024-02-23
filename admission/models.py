from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.


class Applicant(models.Model):
    profile_picture = models.ImageField(
        upload_to='profile_pics/', null=True, blank=True)
    name = models.CharField("Student Name", max_length=50)
    email_id = models.EmailField("Email Id", unique=True, max_length=100)
    date_of_birth = models.DateField()
    address = models.TextField()
    tenth_mark = models.IntegerField('10th', validators=[
        MinValueValidator(175),
        MaxValueValidator(500)
    ])
    twelveth_mark = models.IntegerField('12th', validators=[
        MinValueValidator(270),
        MaxValueValidator(600)
    ])
    contact_number = models.CharField(max_length=15)
    emergency_contact_name = models.CharField(max_length=30)
    emergency_contact_number = models.CharField(max_length=15)
    gender = models.CharField(max_length=10, blank=True, null=True, choices=[(
        'Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')])
    nationality = models.CharField(max_length=50)
    religion = models.CharField(max_length=50)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class ApplicationDocuments(models.Model):
    name = models.CharField("Document Name", max_length=100)
    document = models.FileField("Document", upload_to="application_documents/")
    applicant = models.ForeignKey(
        Applicant, on_delete=models.CASCADE, related_name="documents")
