import email
from logging import PlaceHolder
from django import forms
class SubscribeForm(forms.Form):
    email = forms.EmailField()