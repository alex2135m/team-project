from django.contrib import admin
from .models import List


class ListAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'rating')
    list_display_links = ('title', 'description', 'rating')
    search_fields = ('title', 'rating')


admin.site.register(List, ListAdmin)
