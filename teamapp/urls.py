from django.urls import path
from . import views


# маршруты уровня приложения с вложенным списком маршрутов
urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:list_id>/', views.list_detail, name='detail'),
    path('add/', views.add, name='add'),
]
