from django import forms

class iniciar_sesion(forms.Form):

    user = forms.CharField(max_length=40)
    password = forms.CharField(max_length=20)