from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    # return HttpResponse('zhuye')
    return render(request, 'index.html')