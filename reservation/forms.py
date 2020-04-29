from django import forms

class ReservationForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    occation = forms.S