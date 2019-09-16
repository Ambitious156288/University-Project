from django.shortcuts import render
from django.http import HttpResponse
from .models import Odnosnik

links = [
    {
        'name':'Facebook',
        'link':'https://www.facebook.com/RzeszowskieJuwenalia/',
        'image':'/media/fb.jpg'
    },
    {
        'name':'Instagram',
        'link':'https://www.instagram.com/RzeszowskieJuwenalia/',
        'image':'/media/insta.jpg'
    }
]

def home(request):
    context = {
        'links': Odnosnik.objects.all()
    }
    return render(request, 'odnosniki/home.html', context)
    #return render(request, '<h1>asd</h1>', context)