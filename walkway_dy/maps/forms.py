from django import forms

class LocationForms(forms.Form):
    longtitude = forms.FloatField()
    latitude = forms.FloatField()