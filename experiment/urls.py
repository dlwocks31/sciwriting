from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('main', views.main, name='main'),
    path('end', views.end, name='end'),
    path('postdata', views.postdata, name='postdata'),
    path('postinfo', views.postinfo, name='postinfo'),
    path('endend', views.endend, name='endend'),
    path('lotto', views.lotto, name='lotto'),
    path('keyboard', views.keyboard, name='keyboard')
    path('message', views.message, name='message')
]