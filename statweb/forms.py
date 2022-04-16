import email
from email import message
from logging import PlaceHolder
from django import forms
class SubscribeForm(forms.Form):
    email = forms.EmailField()

class ContactForm(forms.Form):
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)