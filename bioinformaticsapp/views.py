from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from bioinformaticsapp.forms import DnaForm
from random import choice
from django.core.files import File
import subprocess as sp
from Bio.Seq import Seq
from part11 import My_randomseq

# set homepage
def homeroot(request):
    return HttpResponse("<h1>This is the homepage, please click <a href=' ./bio'> here </a> to continue </h1>")

def hello(request):
    return render(request, 'test')

# define request.method == 'get' to get this user input number
# put this number to variable length and generate a random DNA sequence with this length

def bioinformatics(request):
    randomseq = ''
    myRandomseq = ''
    myRCSeq = ''
    myProtein = ''
    if request.method == "POST":
        inputlength = request.POST.get('length', None)
        length = DnaForm(inputlength)
        if length.is_valid():
            l=length.cleaned_data['length']
            for i in range(l):
                randomseq += choice('ATCG')
                return randomseq
            myRandomseq=Seq(randomseq)
            myRCSeq = My_randomseq.rev_c(myRandomseq)
            myProtein=My_randomseq.protein(myRCSeq)

    myRandomseq={'myRandomseq':myRandomseq}
    myRCSeq={'myRCSeq': myRCSeq}
    myProtein={'myProtein': myProtein }

    return render(request, 'bio.html', myRandomseq, myRCSeq, myProtein )
