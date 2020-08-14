from django.shortcuts import render
from .models import List


def index(request):
    lists = List.objects.all()
    context = {'lists': lists}
    return render(request, 'teamapp/index.html', context)


def top(request):
    tops = List.objects.order_by('-rating')[:1]
    context = {'tops': tops}
    return render(request, 'teamapp/top.html', context)
