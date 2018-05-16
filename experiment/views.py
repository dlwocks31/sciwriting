from random import randint

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.exceptions import PermissionDenied
from django.template import loader
from django.views.decorators.http import require_POST

from experiment.models import User, Result, Survey


def index(request):
    if 'referer' not in request.session:
        request.session['referer'] = request.META.get('HTTP_REFERER')
        print('referer:%s' % request.session['referer'])
    request.session['datapostcnt'] = 0
    return render(request, 'experiment/index.html')

def main(request):
    if 'referer' not in request.session:
        raise PermissionDenied
    mode = randint(1, 2)
    return render(request, 'experiment/main%d.html' % mode)

@require_POST
def postdata(request):
    if request.session['datapostcnt'] == 0:
        print(request.POST['data'])
        request.session['datapostcnt'] += 1
    else:
        print('Will save data, although datapostcnt >= 1 already.')
        request.session['datapostcnt'] += 1
    return redirect('end')

@require_POST
def postinfo(request):
    print(request.POST)
    return redirect('endend')

def endend(request):
    if 'referer' not in request.session:
        raise PermissionDenied
    return render(request, 'experiment/endend.html')

def end(request):
    if 'referer' not in request.session or request.session['datapostcnt'] == 0:
        raise PermissionDenied
    return render(request, 'experiment/end.html')
