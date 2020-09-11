from django.shortcuts import render, redirect, get_object_or_404
from .models import List
from .forms import ListForm


# вывод всех записей из БД
# def index(request):
#     lists = List.objects.all()
#     tops = List.objects.order_by('-rating')[:1]
#     context = {'lists': lists, 'tops': tops}
#     return render(request, 'teamapp/index.html', context)


# функция поиска записи по значению ключа
# выводит страницу со сведениями о выбранном посетителем объекта
def list_detail(request, list_id):
    list = get_object_or_404(List, pk=list_id)
    return render(request, 'teamapp/list_detail.html', {'list': list})


# функция, которая создает форму записи данных через шаблон в БД, и выводит список ресторанов.
def index(request):
    lists = List.objects.all()
    tops = List.objects.order_by('-rating')[:1]
    if request.method == "POST":
        form = ListForm(request.POST)
        if form.is_valid():
            list = form.save()
            list.user = request.user
            list.title = request.POST.get('title').capitalize().rstrip()
            list.save()
            return redirect('index')
        else:
            return render(request, 'teamapp/index/html', {'lists': lists, 'tops': tops, 'form': form})
    else:
        form = ListForm()
        return render(request, 'teamapp/index.html', {'lists': lists, 'tops': tops, 'form': form})


# Функция, которая удаляет запись.
def delete(request, pk):
    list = List.objects.get(pk=pk)
    if request.method == "POST":
        list.delete()
        return redirect('index')
    else:
        context = {'list': list}
        return render(request, 'teamapp/list_confirm_delete.html', context)
