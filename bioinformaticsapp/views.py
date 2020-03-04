from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from random import choice
from Bio.Seq import Seq
from django import forms
from bioinformaticsapp.forms import DnaForm

# set homepage
def homeroot(request):
    return HttpResponse("<h1>This is the homepage, please click <a href=' ./input'> here </a> to continue </h1>")

def hello(request):
    return render(request, 'test')

# define request.method == 'get' to get this user input number
# put this number to variable length and generate a random DNA sequence with this length

def bioinformatics(request):
    sequence = ''
    if request.method == "get":
        l = request.GET.get('length')
        l = DnaForm(l)
        if l.is_valid():
            l = DnaForm.cleaned_data['l']
            for i in range(l):
                sequence += choice('ATCG')
            return sequence
    return render(request,'input.html',{'length':sequence} )
