from django.shortcuts import render
from .models import List
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from .forms import ListForm
from django.urls import reverse_lazy


# вывод всех записей из БД
def index(request):
    lists = List.objects.all()
    tops = List.objects.order_by('-rating')[:1]
    context = {'lists': lists, 'tops': tops}
    return render(request, 'teamapp/index.html', context)


# вывод страницы с самым высоким рейтингом
def top(request):
    tops = List.objects.order_by('-rating')[:1]
    context = {'tops': tops}
    return render(request, 'teamapp/top.html', context)


# класс поиска записи по значению ключа
# выводит страницу со сведениями о выбранном посетителем объекта
class ListDetailView(DetailView):
    model = List

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lists'] = List.objects.all()
        return context


#
class ListCreateView(CreateView):
    template_name = 'teamapp/create.html'
    form_class = ListForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lists'] = List.objects.all()
        return context