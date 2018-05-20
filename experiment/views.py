from random import randint

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.exceptions import PermissionDenied
from django.template import loader
from django.views.decorators.http import require_POST
from django.utils import timezone
from ipware import get_client_ip

from experiment.models import User, Result, Survey


def index(request):
    if 'uid' not in request.session or not User.objects.filter(pk=request.session['uid']):
        referer = request.META.get('HTTP_REFERER') or ''
        useragent = request.META.get('HTTP_USER_AGENT') or ''
        ip, is_routable = get_client_ip(request) or ''
        u = User(ipaddr=ip, useragent=useragent, referer=referer)
        u.save()
        request.session['uid'] = u.id
        request.session['datapostcnt'] = 0
        print('User with uid=%d generated. ip="%s", useragent="%s", referer="%s"' % (u.id,ip,useragent,referer))
    print('index loaded. uid is %d' % request.session['uid'])
    return render(request, 'experiment/index.html')

def main(request):
    if 'uid' not in request.session:
        raise PermissionDenied
    mode = randint(1, 2)
    print('main loaded. uid is %d' % request.session['uid'])
    return render(request, 'experiment/main%d.html' % mode)

@require_POST
def postdata(request):
    if 'uid' not in request.session:
        raise PermissionDenied
    print('postdata called by uid=%d.data=%s'%(request.session['uid'], request.POST.get('data')))
    u = User.objects.get(id=request.session['uid'])
    r = Result(uid=u, 
               date=timezone.now(),
               data=request.POST.get('data'),
               postcnt=request.session['datapostcnt'])
    r.save()
    if request.session['datapostcnt'] == 0:
        print('Is first post')
        u.firstresult = r
        u.save()
    else:
        print('Is NOT a first post')
    request.session['datapostcnt'] += 1
    return redirect('end')

@require_POST
def postinfo(request):
    if 'uid' not in request.session:
        raise PermissionDenied
    u = User.objects.get(pk=request.session['uid'])
    poster = True if 'poster' in request.POST else False
    email = request.POST['email'] if poster else ''
    lotto = True if 'lotto' in request.POST else False
    phone = request.POST['phone'] if lotto else ''
    print('info posted by uid=%d. poster=%d,lotto=%d,email="%s",phone="%s".'%(request.session['uid'],poster,lotto,email,phone))
    s = Survey(is_poster=poster, 
               is_lotto=lotto,
               email=email,
               phone=phone)
    s.save()
    u.survey = s
    u.save()
    return redirect('endend')

def endend(request):
    if 'uid' not in request.session:
        raise PermissionDenied
    return render(request, 'experiment/endend.html')

def end(request):
    if 'uid' not in request.session or request.session['datapostcnt'] == 0:
        raise PermissionDenied
    print('end loaded by uid=%d' % request.session['uid'])
    return render(request, 'experiment/end.html')
