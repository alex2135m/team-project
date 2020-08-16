from django.urls import path
from . import views
from .views import ListDetailView

urlpatterns = [
    path('', views.index, name='index'),
    path('top/', views.top, name='top'),
    path('detail/<int:pk>/', ListDetailView.as_view(), name='detail'),
]
