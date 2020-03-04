from django import forms

def input_check(length):
    return type(length)

# creating a class named DnaForm, each feild would be mapped as an input field in html
# input filed including IntegerFeild, FileInputFeild

class DnaForm(forms.Form):
    length=forms.IntegerField(label='Length')
    file=forms.FileField(label="File")

# use clean method to define validation rules
def clean_length(self):
    length=self.cleaned_data.get('length')
    if input_check(length):
        t=input_check(length)
        if t != int:
            raise forms.ValidationError ('It is not an integer')
    else:
        raise forms.ValidationError('Please enter an inter')
    return length






