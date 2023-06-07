from django.shortcuts import render
from .models import *


def index(request):
    new = News.objects.all()
    context = {'new':new}
    return render(request, 'blog/index.html', context)
# Create your views here.
