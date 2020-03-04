from django.shortcuts import render
from django.http import HttpResponse

def bioinformatics(request):
    return render(request,'demo.html')

