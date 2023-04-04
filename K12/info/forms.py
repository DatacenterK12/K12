from django import forms
from phonenumber_field.formfields import PhoneNumberField


class PhoneForm(forms.Form):
    name = forms.CharField(max_length=100)
    subject = forms.CharField(max_length=500)
    phone = PhoneNumberField(region="RU")
