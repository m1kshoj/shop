from django.db import models


class Article(models.Model):  # таблица из бд
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")  # Y m d - год, месяц, день
    timeCreate = models.DateTimeField(auto_now_add=True)  # меняется 1 раз при создании
    timeUpdate = models.DateTimeField(auto_now=True)  # меняется когда запись редактируется
    isPublished = models.BooleanField(default=True)
