from django.forms import ModelForm
from .models import List


# создание формы, связанную с моделью List
class ListForm(ModelForm):

    # функция, которая автоматически делает название с заглавной буквой
    def clean_title(self):
        return self.cleaned_data['title'].capitalize()

    # параметры формы,
    # поля, которые присутствуют в форме
    class Meta:
        model = List
        fields = ('author', 'title', 'description', 'address', 'mailbox', 'rating')
