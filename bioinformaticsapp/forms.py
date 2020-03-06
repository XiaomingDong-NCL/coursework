from django import forms
from django.db import models
from bioinformaticsapp.models import Integerlength

class BioForm(forms.ModelForm):
    integerlength = forms.IntegerField(label='length')

    class Meta:
        model = Integerlength
        fields = ('integerlength',)



