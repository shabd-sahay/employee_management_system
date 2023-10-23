from django import forms
from shabd.models import Employee
from shabd.models import Company
from shabd.models import Login
# This is for employee
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = "__all__"

class loginForm(forms.ModelForm):
    class Meta:
        model = Login
        fields = "__all__"