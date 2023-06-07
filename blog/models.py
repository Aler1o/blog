from django.db import models

class News(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название")
    content = models.TextField(verbose_name="Текст")
    author = models.CharField(max_length=250, verbose_name="Автор")
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name= 'Новость'
        verbose_name_plural= 'Новости'    

# Create your models here.
