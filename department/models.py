from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class AcademicProgram(models.Model):
    name = models.CharField("Program", max_length=100)
    code = models.CharField("Code", max_length=20, unique=True)

    def __str__(self):
        return self.name


class Department(models.Model):
    department_name = models.CharField("Department Name", max_length=15)

    def __str__(self) -> str:
        return self.department_name


class Course(models.Model):
    name = models.CharField("Course Name", max_length=50)
    code = models.CharField("Course Code", max_length=20, unique=True)
    description = models.TextField("Course Description")
    program = models.ForeignKey(AcademicProgram, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Classroom(models.Model):
    name = models.CharField("Classroom", max_length=50)

    def __str__(self):
        return self.name
