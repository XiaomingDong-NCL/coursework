from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from random import choice
from Bio.Seq import Seq
from django import forms
from bioinformaticsapp.forms import DnaForm

# transfer the input number to random sequence and store it in randomdna.txt file
# define request.method == 'get' to get this sequence

def bioinformatics(request):
    if request.method == "GET":
        length = DnaForm(request.GET or None)
        if length.is_valid():
            length=DnaForm.changed_data['length']
            for i in range(length):
                sequence = ''
                sequence += choice('ATCG')
                return sequence
    return render(request,'demo.html',{'length':length} )




