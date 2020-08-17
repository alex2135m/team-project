from django.db import models


# представление строк в БД
class List(models.Model):
    title = models.CharField('Название', max_length=100)
    description = models.TextField('Описание')
    address = models.CharField('Адрес ресторана', max_length=150, null=True)
    mailbox = models.EmailField('E-mail', max_length=100, null=True)
    rating = models.FloatField('Рейтинг')
    objects = models.Manager()

# возвращение строкового представления модели
    def __str__(self):
        return self.title

# параметры самой модели
# сортировка по названию
    class Meta:
        ordering = ['-title']
