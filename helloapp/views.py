from django.shortcuts import render
from django.http import HttpResponse
def hello(request):
    html= "<h1> Interested in how it works ? </h1>" \
          "<h2> Please find me on GitHub. https://github.com/XiaomingDong-NCL/coursework  </h2>"
    return HttpResponse(html)
