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
    datalist = []
    if request.method == "POST":
        length = request.GET.get('length', None)
        with open ('results.txt','w') as f:
            myseq = randomseq(length)
            myseq_s = My_randomseq(myseq)
            myseq_rc = My_randomseq.rev_c(myseq)
            myseq_p = My_randomseq.protein(myseq)
            f.write("{}--{}--{}".format(myseq_s, myseq_rc, myseq_p))
        return render(request, 'bio.html')
    if request.method == "GET" and 'myRandomseq':
        with open ('results.txt','r') as f:
            for line in f :
                result = line.split('--')
                datalist.append(result)
        myRandomseq = {'myRandomseq': datalist}
        return render(request, 'bio.html', myRandomseq)
    if request.method == "GET" and 'myRCSeq':
        with open ('results.txt','r') as f:
            for line in f :
                result = line.split('--')
                datalist.append(result)
        myRCSeq = {'myRCSeq': datalist}
        return render(request, 'bio.html', myRCSeq)
    if request.method == "GET" and 'myProtein':
        with open ('results.txt','r') as f:
            for line in f :
                result = line.split('--')
                datalist.append(result)
        myProtein = {'myProtein': datalist}
        return render(request, 'bio.html', myProtein)
