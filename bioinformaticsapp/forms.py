from django import forms
from django.db import models
from bioinformaticsapp.models import Integerlength
from part1without_input import My_randomseq, randomseq

class BioForm(forms.ModelForm):
    integerlength = forms.IntegerField()

    class Meta:
        model = Integerlength
        fields = ('integerlength',)

