from django.shortcuts import render
from django.http import HttpResponse
from random import choice
from Bio.Seq import Seq

# transfer the input number to random sequence and store it in randomdna.txt file
# define request.method == 'get' to get this sequence
def bioinformatics(request):
    if request.method == 'post':
        i=request.post.get("integer", None)
        with open('randomdna.txt', 'a+') as f:
            sequence = ''
            for i in range(int(i)):
                sequence += choice('ATCG')
            f.write("{}".format(sequence))
    if request.method == 'get':
        with open('randomdna.txt', 'r') as f:
            randomdna=f.readlines()
    return render(request,'demo.html', {'data': randomdna})

