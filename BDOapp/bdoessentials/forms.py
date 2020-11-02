from django.forms import ModelForm
from bdoessentials.models import Lead
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class DateInput(forms.DateInput):
    input_type = 'date'

class LeadCreateFrm(ModelForm):
    class Meta:
        model=Lead
        fields = '__all__'
        widgets = {
            'leadId': forms.TextInput(attrs={'class': 'form-control'}),
            'leadName': forms.TextInput(attrs={'class': 'form-control'}),
            'phone1': forms.TextInput(attrs={'class': 'form-control'}),
            'company': forms.TextInput(attrs={'class': 'form-control'}),
            'contactPerson': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'leadRegisterDate': DateInput(),
            'phone2': forms.TextInput(attrs={'class': 'form-control'}),
            'leadSource': forms.TextInput(attrs={'class': 'form-control'}),
            'leadIndustry': forms.TextInput(attrs={'class': 'form-control'}),
            'officeAddress': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'notes': forms.TextInput(attrs={'class': 'form-control'}),
        }

    # def clean_leadId(self):
    #     leadId = self.cleaned_data.get('leadId')
    #     for instance in Lead.objects.all():
    #         if instance.leadId == leadId:
    #             raise forms.ValidationError(leadId + 'already exists')
    #     return leadId
    # def clean_email(self):
    #     email = self.cleaned_data.get('email')
    #     for instance in Lead.objects.all():
    #         if instance.email == email:
    #             raise forms.ValidationError(email + 'already exists')
    #     return email
    #
    # def clean_phone1(self):
    #     phone1 = self.cleaned_data.get('phone1')
    #     for instance in Lead.objects.all():
    #         if instance.phone1 == phone1:
    #             raise forms.ValidationError(phone1 + 'already exists')
    #     return phone1
    #
    # def clean_phone2(self):
    #     phone2 = self.cleaned_data.get('phone2')
    #     for instance in Lead.objects.all():
    #         if instance.phone2 == phone2:
    #             raise forms.ValidationError(phone2 + 'already exists')
    #     return phone2


class RegistrationFrm(UserCreationForm):
    class Meta:
        model=User
        fields=['first_name','username','last_name','email','password1','password2']

