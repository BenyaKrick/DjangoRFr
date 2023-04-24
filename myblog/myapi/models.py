from django.db import models
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=80, db_index=True, verbose_name="Рубрика")

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Рубрика'
        verbose_name_plural = 'Рубрики'


class Post(models.Model):
    category = models.ForeignKey(
        'Category', on_delete=models.PROTECT, blank=True, null=True, verbose_name='Рубрики')
    title = models.CharField(max_length=100)
    description = models.TextField()
    author = models.CharField(max_length=100)
    date = models.DateField(blank=True, null=True)
    img = models.ImageField(upload_to='image/%Y%M%D', blank=False)

    def __str__(self):
        return f'{self.title}, {self.author}'

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'


class Comments(models.Model):
    post = models.ForeignKey(
        'Post', on_delete=models.CASCADE, blank=True, null=True, verbose_name='Пост')
    description = models.TextField()
    author = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.description, self.author}'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
