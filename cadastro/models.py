from django import forms

class Register(forms.Form):
    name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.CharField(max_length=100)
    cpf = forms.IntegerField()
    phone_number = forms.IntegerField()
    age = forms.IntegerField()
    gender = forms.BooleanField()