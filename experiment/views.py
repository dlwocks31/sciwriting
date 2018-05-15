from random import randint

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.http import require_POST


def index(request):
    return render(request, 'experiment/index.html')

def main(request):
    mode = randint(1, 2)
    return render(request, 'experiment/main%d.html' % mode)

@require_POST
def postdata(request):
    print(request.POST['data'])
    return redirect('end')


def end(request):
    return render(request, 'experiment/end.html')
