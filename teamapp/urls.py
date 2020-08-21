from django.urls import path
from . import views
from .views import ListDetailView


# маршруты уровня приложения с вложенным списком маршрутов
urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:pk>/', ListDetailView.as_view(), name='detail'),
    path('add/', views.add, name='add'),
]
