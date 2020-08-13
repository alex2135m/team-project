from django.db import models


class List(models.Model):
    title = models.CharField('Название', max_length=100)
    description = models.TextField('Описание')
    rating = models.FloatField('Рейтинг')
    # objects = models.Manager()

    def __str__(self):
        return self.title
