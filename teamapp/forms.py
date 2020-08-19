from django.forms import ModelForm
from .models import List


# создание формы, связанную с моделью List
class ListForm(ModelForm):

    class Meta:
        model = List
        fields = ('author', 'title', 'description', 'address', 'mailbox', 'rating')
