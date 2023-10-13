from django.db import models
from django.contrib.auth.models import User
from department.models import Course, Classroom
from staff.models import Staff


class Student(models.Model):
    profile_picture = models.ImageField(
        upload_to='profile_pics/', null=True, blank=True)
    user_name = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='student', null=True, blank=True)
    date_of_birth = models.DateField()
    address = models.TextField()
    tenth_mark = models.CharField('10th', max_length=3)
    twelveth_mark = models.CharField('12th', max_length=3)
    contact_number = models.CharField(max_length=15)
    emergency_contact_name = models.CharField(max_length=30)
    emergency_contact_number = models.CharField(max_length=15)
    gender = models.CharField(max_length=10, choices=[(
        'Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')])
    nationality = models.CharField(max_length=50)
    religion = models.CharField(max_length=50)

    def __str__(self):
        if self.user_name is None:
            return super().__str__()
        return self.user_name.username


class StudentDocuments(models.Model):
    name = models.CharField("Document Name", max_length=100)
    document = models.FileField("Document", upload_to="student_documents/")
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name="documents", null=True, blank=True)


class Attendance(models.Model):
    student_attendance = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, null=True, blank=True)
    class_room = models.ForeignKey(
        Classroom, on_delete=models.CASCADE, null=True, blank=True
    )
    date = models.DateField()
    status = models.CharField(max_length=10, default=None, choices=[
        ('Present', 'Present'), ('Absent', 'Absent')
    ])

    def __str__(self) -> str:
        return f"{self.student_attendance.user_name}"


class AcademicRecords(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    class_room = models.ForeignKey(
        Classroom, on_delete=models.CASCADE, null=True, blank=True
    )
    marks = models.DecimalField('Marks', max_digits=5, decimal_places=2)
    grade = models.CharField('Grade',  max_length=5)
    teacher_comments = models.TextField(
        "Teacher Comments", null=True, blank=True)
    year = models.CharField("year", max_length=4)
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, null=True, blank=True)
    subject_code = models.CharField("Subject Code", max_length=10)
    attendance_percentage = models.DecimalField(
        "Attendance Precentage", max_digits=5, decimal_places=2)

    def __str__(self) -> str:
        return f"{self.student.user_name}'s"


class Perfromance(models.Model):
    student_name = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.CharField("Subject", max_length=50)
    class_room = models.ForeignKey(
        Classroom, on_delete=models.CASCADE, null=True, blank=True
    )
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, null=True, blank=True)
    marks = models.DecimalField("Marks", max_digits=5, decimal_places=2)
    grade = models.CharField("Grade", max_length=5, choices=[
        ('o', 'o'),
        ('A+', 'A+'),
        ('A', 'A'),
        ('B+', 'B+'),
        ('B', 'B'),


    ])
    remarks = models.TextField("Remarks", null=True, blank=True)
    exam_date = models.DateField()
    teacher_feedback = models.TextField(
        "Teacher Feedback", null=True, blank=True)
    project_score = models.DecimalField(
        "Project Score", max_digits=5, decimal_places=2, null=True, blank=True)
    participation_level = models.CharField(
        "Participation  Level", max_length=20, null=True, blank=True)
    additional_comments = models.TextField(
        "Additional Comments", null=True, blank=True)
    test_1_score = models.DecimalField(
        " Test 1 Score", max_digits=5, decimal_places=2, null=True, blank=True)
    test_2_score = models.DecimalField(
        "Test 2 Score", max_digits=5, decimal_places=2, null=True, blank=True)
    final_exam_score = models.DecimalField(
        "Final Exam Score", max_digits=5, decimal_places=2, null=True, blank=True)
    practical_exam_score = models.DecimalField(
        "Prartical Exam Score", max_digits=5, decimal_places=2, null=True, blank=True)
    assignment_score = models.DecimalField(
        "Assignment Score", max_digits=5, decimal_places=2, null=True, blank=True)
    presentation_score = models.DecimalField(
        "Presentation Score", max_digits=5, decimal_places=2, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.student_name.user_name}"


class Leave(models.Model):
    start_date = models.DateField("Strart Date")
    end_date = models.DateField("end Date")
    student_leave = models.ForeignKey(Student, on_delete=models.CASCADE)
    reason = models.TextField("Reason", max_length=200)
    leave_status = models.CharField('Leave Status', max_length=1, default="P", choices=[
        ('P', 'Pending'),
        ('A', 'Approved'),
        ('D', 'Denied')
    ])

    def __str__(self) -> str:
        return f"{self.student_leave.user_name}"
