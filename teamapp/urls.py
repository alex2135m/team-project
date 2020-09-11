from django.urls import path
from . import views
# from .views import ListDeleteView


# маршруты уровня приложения с вложенным списком маршрутов
urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:list_id>/', views.list_detail, name='detail'),
    path('', views.index, name='add'),
    # path('delete/<int:pk>/', ListDeleteView.as_view(), name='delete'),
    path('delete/<int:pk>/', views.delete, name='delete')
]
