from django.shortcuts import render, redirect
from .models import List
from django.views.generic.detail import DetailView
from .forms import ListForm


# вывод всех записей из БД
def index(request):
    lists = List.objects.all()
    tops = List.objects.order_by('-rating')[:1]
    context = {'lists': lists, 'tops': tops}
    return render(request, 'teamapp/index.html', context)


# класс поиска записи по значению ключа
# выводит страницу со сведениями о выбранном посетителем объекта
class ListDetailView(DetailView):
    model = List

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lists'] = List.objects.all()
        return context


# функция, которая создает форму записи данных через шаблон в БД
def add(request):
    if request.method == "POST":
        form = ListForm(request.POST)
        if form.is_valid():
            list = form.save()
            list.author = request.user
            list.save()
            return redirect('index')
    else:
        form = ListForm()
        return render(request, 'teamapp/add.html', {'form': form})
