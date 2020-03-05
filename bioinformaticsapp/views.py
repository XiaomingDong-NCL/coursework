from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from bioinformaticsapp.forms import DnaForm
from random import choice
from django.core.files import File
import subprocess as sp
from Bio.Seq import Seq

# set homepage
def homeroot(request):
    return HttpResponse("<h1>This is the homepage, please click <a href=' ./bio'> here </a> to continue </h1>")

def hello(request):
    return render(request, 'test')

# define request.method == 'get' to get this user input number
# put this number to variable length and generate a random DNA sequence with this length

def bioinformatics(request):
    if request.method == "POST":
        inputlength = request.POST.get('length', None)
        length = DnaForm(inputlength)
        if length.is_valid():
            l=length.cleaned_data['length']
            sequence = ''
            for i in range(l):
                sequence += choice('ATCG')
        with open('../coursework/results.txt', 'a+') as f:
            f.write('{}'.format(sequence))
    if request.method == 'GET':
        mydan=''
        with open('../coursework/results.txt', 'r') as f:
            seq=''
            for line in f:
                seq.append(line)
                mydan=seq
    return render(request, 'bio.html',{'seq':mydan})

