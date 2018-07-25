from django import forms
from .models import Student
from django.forms import ModelForm

class StudentForm(forms.ModelForm):
    # name = forms.CharField(max_length=255)
    # mark = forms.CharField(max_length=255)
    class Meta:
        model = Student
        fields = '__all__' #['name','mark',]


class StudentFormset:
    pass