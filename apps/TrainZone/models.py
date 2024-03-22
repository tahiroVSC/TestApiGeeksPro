from django.db import models
from ckeditor.fields import RichTextField
from django_resized import ResizedImageField
# Create your models here.

class TrainZone(models.Model):
    photo = ResizedImageField(force_format="WEBP", quality=100, verbose_name="Фотография",blank = True, null = True)
    title = models.CharField(max_length=100, verbose_name='Название')
    description = RichTextField(verbose_name='Описание')


    def __str__(self):
        return self.title



    class Meta:
        verbose_name = 'Зона',
        verbose_name_plural = 'Зоны'