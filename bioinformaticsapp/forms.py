from django import forms

# creating a DnaForm, each feild would be mapped as an input field in html
# input filed including integer feild, FileInput feild

class DnaForm(forms.Form):
    length=forms.IntegerField()
    file=forms.FileField()
