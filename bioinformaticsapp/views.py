from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
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
