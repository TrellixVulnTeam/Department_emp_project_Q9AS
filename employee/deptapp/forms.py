from django import forms
from .models import Department, Employee

class AddForm(forms.ModelForm):

    class Meta:
        model = Department
        fields = ('deptname','dept_logo')

class EmpForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ('empname', 'emplastname', 'empsal')