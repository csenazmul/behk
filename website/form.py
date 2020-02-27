from django import forms
from .models import *
# Contact Form
class ContactForm(forms.Form):
    contact_name = forms.CharField(required = True)
    contact_email = forms.EmailField(required = True)
    content = forms.CharField(required = True)
