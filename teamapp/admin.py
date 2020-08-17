from django.contrib import admin
from .models import List


# отредактированное представление модели на административной панели,
# редактор объявляется как подкласс класса ModelAdmin из модуля django.contrib.admin
class ListAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'address', 'mailbox', 'rating')
    list_display_links = ('title', 'description')
    search_fields = ('title', 'rating')


# регистрация приложения в административной панели
admin.site.register(List, ListAdmin)
