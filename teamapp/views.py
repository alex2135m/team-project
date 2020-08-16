from django.shortcuts import render
from .models import List
from django.views.generic.detail import DetailView


def index(request):
    lists = List.objects.all()
    context = {'lists': lists}
    return render(request, 'teamapp/index.html', context)


def top(request):
    tops = List.objects.order_by('-rating')[:1]
    context = {'tops': tops}
    return render(request, 'teamapp/top.html', context)


class ListDetailView(DetailView):
    model = List

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lists'] = List.objects.all()
        return context