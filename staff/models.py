from django.db import models
from django.contrib.auth.models import User
from department.models import Course, AcademicProgram, Classroom
# Create your models here.


class Staff(models.Model):
    profile_picture = models.ImageField(
        upload_to='profile_pics/', null=True, blank=True)
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='staff')
    email_id = models.EmailField(
        "Email Id", max_length=100, blank=True, null=True)
    department = models.ForeignKey(
        'department.Department', on_delete=models.CASCADE, blank=True, null=True)
    teaching_type = models.CharField("Teaching Type", max_length=3, default=None, choices=[
        ('HOD', 'Hod'),
        ('P', 'Professor'),
        ('AP', 'Assistant Professor'),
        ('LS', 'Lab Staff')
    ])
    qualifications = models.CharField(
        'Qualifications', max_length=50, null=True, blank=True)
    experience = models.CharField("Experience", max_length=10)
    contact_number = models.CharField(
        'Contact Number', max_length=15,  null=True, blank=True)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10, choices=[(
        'Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')])
    marital_status = models.CharField(max_length=10, choices=[(
        'Married', 'Married'), ('Un Married', 'Un Married')])
    nationality = models.CharField(max_length=50)
    religion = models.CharField(max_length=50)
    address = models.TextField()
    # roles = models.ManyToManyField(Role)

    def __str__(self):
        return self.user.first_name


class Training(models.Model):

    name = models.CharField("Training Name", max_length=50)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    start_date = models.DateField("Start Date")
    end_date = models.DateField('End Date')
    description = models.TextField("Description", max_length=200)
    request_status = models.CharField('Request Status', max_length=1, default="P", choices=[
        ('P', 'Pending'),
        ('A', 'Approved'),
        ('D', 'Denied')

    ])

    def __str__(self) -> str:
        return self.name


class PerfromanceEvulation(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    goalsetting = models.TextField('Goals', max_length=100)
    assessments = models.TextField('Assessments', max_length=100)
    feedback = models.TextField("Feedback", max_length=200)

    def __str__(self):
        return self.staff.__str__()


class Degree(models.Model):
    degree_name = models.CharField('Degree', max_length=5, default=None)

    def __str__(self):
        return self.degree_name


class Qualification(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    degree = models.ForeignKey(Degree, on_delete=models.CASCADE)
    branch = models.CharField('Branch', max_length=20)
    instituition = models.CharField('Instituition', max_length=150)
    year_passing = models.CharField(
        'Year Passing', max_length=9, help_text="eg: 2020-2024")

    def __str__(self):
        return self.staff.__str__()


class Leave(models.Model):
    start_date = models.DateField("Strart Date")
    end_date = models.DateField("end Date")
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    reason = models.TextField("Reason", max_length=200)
    leave_status = models.CharField('Leave Status', max_length=1, default="P", choices=[
        ('P', 'Pending'),
        ('A', 'Approved'),
        ('D', 'Denied')
    ])

    def __str__(self) -> str:
        return self.staff.__str__()


class EmergencyContact(models.Model):
    name = models.CharField('Name', max_length=30)
    relationship = models.CharField('Relationship', max_length=30)
    phone = models.CharField('Phonenumber', max_length=15)
    # email = models.EmailField('Email Id', max_length=40)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class ClassSchecule(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    academic_program = models.ForeignKey(
        AcademicProgram, on_delete=models.CASCADE)
    staff = models.ForeignKey('staff.Staff', on_delete=models.CASCADE)
    class_room = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    day = models.CharField("Day", max_length=10, choices=[
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday')
    ])
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.course} - {self.day} - {self.start_time} to {self.end_time}"
