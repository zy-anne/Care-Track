from django import forms


class Patient(forms.Form):
    your_name = forms.CharField(label="Your name", max_length=100)