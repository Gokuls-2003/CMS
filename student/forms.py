from .models import Perfromance, AcademicRecords, Leave
from django import forms
from django.core.exceptions import ValidationError
from datetime import date


class PerfromanceForm(forms.ModelForm):

    class Meta:
        models = Perfromance
        # fields = ("student_name", 'subject', 'class_room',
        #           'course', 'marks', 'grade', 'remarks', 'exam_date', 'teacher_feedback', 'project_score', 'participation_level',
        #           'additional_comments', 'test_1_score', 'test_2_score', 'final_exam_score', 'practical_exam_score', 'assignment_score', 'presentation_score')
        fields = "__all__"

    def clean_subject(self):
        subject = self.cleaned_data["subject"]

        if not subject:
            raise ValidationError("subject is required")

        if not subject.replace(' ', '').isalpha():
            raise forms.ValidationError(
                "Subject can only contain letters and spaces.")

        return subject

    def clean_remarks(self):
        remarks = self.cleaned_data["remarks"]

        if not remarks:
            raise ValidationError("remarks is required")

        words = remarks.split()

        if len(words) > 100:
            raise ValidationError("remarks only contains 100 words")

        for word in words:
            if len(word) >= 10:
                raise ValidationError(
                    "remarks does not support 10  consecutive characters.")

        return remarks

    def clean_teacher_feedback(self):
        teacher_feedback = self.cleaned_data["teacher_feedback"]

        if not teacher_feedback:
            raise ValidationError("remarks is required")

        words = teacher_feedback.split()

        if len(words) > 100:
            raise ValidationError("Teacher feedback only contains 100 words")

        for word in words:
            if len(word) >= 10:
                raise ValidationError(
                    "Teacher feedback does not support 10  consecutive characters.")

        return teacher_feedback

    def clean_additional_comments(self):
        additional_comments = self.cleaned_data["additional_comments"]

        if not additional_comments:
            raise ValidationError("remarks is required")

        words = additional_comments.split()

        if len(words) > 100:
            raise ValidationError("Teacher feedback only contains 100 words")

        for word in words:
            if len(word) >= 10:
                raise ValidationError(
                    "Teacher feedback does not support 10  consecutive characters.")

        return additional_comments

    def clean_project_score(self):
        project_score = self.cleaned_data["project_score"]

        if not project_score or not project_score.isdigit():
            raise ValidationError(
                "Project Score must contain only digits and have at least one digit.")

        if project_score:
            # Check if the number has exactly 10 digits
            if len(project_score) >= 100:
                raise ValidationError(
                    "project score must have exactly 10 digits.")

        return project_score

    def clean_test_1_score(self):
        test_1_score = self.cleaned_data["test_1_score"]

        if not test_1_score or not test_1_score.isdigit():
            raise ValidationError(
                "Test 1 score must contain only digits and have at least one digit.")

        if test_1_score:
            # Check if the number has exactly 10 digits
            if len(test_1_score) >= 100:
                raise ValidationError(
                    "Test 2 must have less than or equal to 100 marks.")

        return test_1_score

    def clean_test_2_score(self):
        test_2_score = self.cleaned_data["test_2_score"]

        if not test_2_score or not test_2_score.isdigit():
            raise ValidationError(
                "Test 2 Score must contain only digits and have at least one digit.")

        if test_2_score:
            # Check if the number has exactly 10 digits
            if len(test_2_score) >= 100:
                raise ValidationError(
                    "Test 2 Score must have less than or equal to 100 marks.")

        return test_2_score

    def clean_final_exam_score(self):
        final_exam_score = self.cleaned_data["final_exam_score"]

        if not final_exam_score or not final_exam_score.isdigit():
            raise ValidationError(
                " Final Exam Score must contain only digits and have at least one digit.")

        if final_exam_score:
            # Check if the number has exactly 10 digits
            if len(final_exam_score) >= 100:
                raise ValidationError(
                    "Final Exam Score must have less than or equal to 100 marks.")

        return final_exam_score

    def clean_practical_exam_score(self):
        practical_exam_score = self.cleaned_data["practical_exam_score"]

        if not practical_exam_score or not practical_exam_score.isdigit():
            raise ValidationError(
                "Pratical Exam Score must contain only digits and have at least one digit.")

        if practical_exam_score:
            # Check if the number has exactly 10 digits
            if len(practical_exam_score) >= 100:
                raise ValidationError(
                    "Pratical Exam Score must have less than or equal to 100 marks.")

        return practical_exam_score

    def clean_assignment_score(self):
        assignment_score = self.cleaned_data["assignment_score"]

        if not assignment_score or not assignment_score.isdigit():
            raise ValidationError(
                "Assignment Score must contain only digits and have at least one digit.")

        if assignment_score:
            # Check if the number has exactly 10 digits
            if len(assignment_score) >= 100:
                raise ValidationError(
                    "Assignment  Score must have less than or equal to 100 marks.")

        return assignment_score

    def clean_presentation_score(self):
        presentation_score = self.cleaned_data["presentation_score"]

        if not presentation_score or not presentation_score.isdigit():
            raise ValidationError(
                "Presentation Score must contain only digits and have at least one digit.")

        if presentation_score:
            # Check if the number has exactly 10 digits
            if len(presentation_score) >= 100:
                raise ValidationError(
                    "Presentation  Score must have less than or equal to 100 marks.")

        return presentation_score

    def clean_participation_level(self):
        participation_level = self.cleaned_data["participation_level"]

        if not participation_level:
            raise ValidationError("Participation Level is required")

        if not participation_level.replace(' ', '').isalpha():
            raise forms.ValidationError(
                "participation_level can only contain letters and spaces.")

        return participation_level


class AcademicRecords(forms.ModelForm):

    class Meta:
        model = AcademicRecords
        fields = '__all__'

    def clean_marks(self):
        marks = self.cleaned_data["marks"]

        if not marks or not marks.isdigit():
            raise ValidationError(
                "marks  must contain only digits and have at least one digit.")

        if marks:
            # Check if the number has exactly 10 digits
            if len(marks) >= 100:
                raise ValidationError(
                    "marks  Score must have less than or equal to 100 marks.")

        return marks

    def clean_teacher_comments(self):
        teacher_comments = self.cleaned_data["teacher_comments"]

        if not teacher_comments:
            raise ValidationError("Teacher Comments is required")

        words = teacher_comments.split()

        if len(words) > 100:
            raise ValidationError("Teacher Comments only contains 100 words")

        for word in words:
            if len(word) >= 10:
                raise ValidationError(
                    "Teacher Comments does not support 10  consecutive characters.")

        return teacher_comments

    def clean_year(self):
        year = self.cleaned_data["year"]

        if not year or not year.isdigit():
            raise ValidationError("Year must contain only digits")

        current_year = date.today().year

    # Check if the year entered by the user is the current year
        if year != current_year:
            raise ValidationError("Year must be the current year.")

        return year

    def clean_subject_code(self):
        subject_code = self.cleaned_data["subject_code"]

        # Check if the subject code is not empty
        if not subject_code:
            raise ValidationError("Subject Code is required")

        # Check if the subject code has more than 10 characters
        if len(subject_code) > 10:
            raise ValidationError(
                "Subject Code must have 10 characters or less")

        # Check if the subject code contains only alphanumeric characters
        if not subject_code.isalnum():
            raise ValidationError(
                "Subject Code must contain only letters and numbers")

        return subject_code

    def clean_attendance_percentage(self):
        attendance_percentage = self.cleaned_data["attendance_percentage"]

        if not attendance_percentage or not attendance_percentage.isdigit():
            raise ValidationError(
                "Attendance Percentage must contain only digits and have at least one digit.")

        if attendance_percentage:
            # Check if the number has exactly 10 digits
            if len(attendance_percentage) >= 100:
                raise ValidationError(
                    "Attendance Percentage must have less than or equal to 100 marks.")

        return attendance_percentage


class LeaveForm(forms.ModelForm):

    class Meta:
        model = Leave
        fields = '__all__'

    def clean_reason(self):
        reason = self.cleaned_data["reason"]

        if not reason:
            raise ValidationError("Reason is Required")

        if not reason.isalnum():
            raise ValidationError(
                "reason must contain only letters and numbers")

        words = reason.split()

        if len(words) > 100:
            raise ValidationError("Reason must contain only 100 Words")

        for word in words:
            if len(word) >= 10:
                raise ValidationError(
                    "Reason does not support 10  consecutive characters. ")

        return reason
