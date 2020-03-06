from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from bioinformaticsapp.forms import BioForm

# set homepage and a link to biopage
def homeroot(request):
    return HttpResponse("<h1>This is the homepage, please click <a href=' ./bio'> here </a> to continue </h1>")

def hello(request):
    return render(request, 'test')

# define request.method == 'get' to get this user input number
# put this number to variable length and generate a random DNA sequence with this length
@csrf_exempt
def bioinformatics(request):
    if request.method == "POST":
        form = BioForm(request.POST)
        if form.is_valid():
            form.save()
            l = form.cleaned_data['length']
        return render(request, 'bio.html')
    else:
        form=BioForm
        return render(request, 'bio.html')

