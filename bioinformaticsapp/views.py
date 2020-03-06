
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from bioinformaticsapp.forms import BioForm
from part1without_input import My_randomseq, randomseq
from bioinformaticsapp.models import Integerlength

# set homepage and a link to the biopage
def homeroot(request):
    return HttpResponse("<h1>This is the homepage, please click <a href=' ./bio'> here </a> to continue </h1>")

# set infopage and show mine github path
def hello(request):
    return render(request, 'info')

# define request.method == 'POST' to get this user input number
# put this number to variable length and generate a random DNA sequence with this length
@csrf_exempt
def bioinformatics(request):
    if request.method == "POST" :
        i= BioForm(request.POST)
        if i.is_valid():
            l = i.cleaned_data['integerlength']
            s = My_randomseq(l)
            r = My_randomseq.rev_c(l)
            p = My_randomseq.protein(l)
            d = {'length':l, 'myRandomseq': s, 'myRCSeq': r, 'myProtein': p}
            d= i. save()
            return redirect(request, 'bio.html', d)

    if request.method == "GET":
        i = BioForm()
        return render(request, 'bio.html' )

