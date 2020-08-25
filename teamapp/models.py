from django.db import models
from django.conf import settings


# представление строк в БД
class List(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default=True, null=True, verbose_name='Автор',
                               on_delete=models.CASCADE)
    title = models.CharField('Название', max_length=100, unique=True)
    description = models.TextField('Описание')
    address = models.CharField('Адрес ресторана', max_length=150, null=True)
    mailbox = models.EmailField('E-mail', max_length=100, null=True, unique=True)
    rating = models.FloatField('Рейтинг')
    objects = models.Manager()

# возвращение строкового представления модели
    def __str__(self):
        return self.title

# функция, которая делает верхний регистр в поле title
#     def save(self, *args, **kwargs):
#         self.title = self.title.capitalize()
#         return super(List, self).save(*args, **kwargs)

# параметры самой модели
# сортировка по рейтингу
    class Meta:
        ordering = ['-rating']
