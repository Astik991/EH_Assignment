from django import forms
from .models import Helper, Customer, Assignment

class HelperForm(forms.ModelForm):
    class Meta:
        model = Helper
        fields = ['name', 'gender', 'skill', 'age']

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'address', 'phone_number']

class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ['helper', 'customer']
