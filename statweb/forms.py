import email
from email import message
from logging import PlaceHolder
from django import forms
class SubscribeForm(forms.Form):
    email = forms.EmailField(label="email",widget=forms.EmailInput(attrs={'placeholder': 'Email Address'}))

class ContactForm(forms.Form):
    email = forms.EmailField(label="email",widget=forms.EmailInput(attrs={'placeholder': 'Email Address'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Message'}))