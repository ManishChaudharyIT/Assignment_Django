from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'dob', 'physics_marks', 'chemistry_marks', 'maths_marks', 'cs_marks']
