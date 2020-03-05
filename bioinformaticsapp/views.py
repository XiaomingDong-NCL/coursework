from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from bioinformaticsapp.forms import DnaForm
from random import choice
from django.core.files import File
import subprocess as sp
from Bio.Seq import Seq
from part1without_input import *
# set homepage
def homeroot(request):
    return HttpResponse("<h1>This is the homepage, please click <a href=' ./bio'> here </a> to continue </h1>")

def hello(request):
    return render(request, 'test')

# define request.method == 'get' to get this user input number
# put this number to variable length and generate a random DNA sequence with this length
@csrf_exempt
def bioinformatics(request):
    if request.method == "POST" and 'length':
        length = request.GET.get('length')
        myRandomseq = randomseq(length)
        myRCSeq = My_randomseq(myRandomseq)
        myRCSeq = My_randomseq.rev_c(myRandomseq)
        myProtein = My_randomseq.protein(myRandomseq)
        length = {'length': length}
        myRandomseq = {'myRandomseq': myRandomseq}
        myRCSeq = {'myRCSeq': myRCSeq}
        myProtein = {'myProtein': myProtein}
        if request.method == "POST" and 'myRandomseq':
            return render(request, 'bio.html', myRandomseq)
        elif request.method == "POST" and 'myRCSeq':
            return render(request, 'bio.html', myRCSeq)
        elif request.method == "POST" and 'myProtein':
            return render(request, 'bio.html', myProtein)

    else :
        return render(request, 'bio.html')