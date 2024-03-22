from django.db import models
from ckeditor.fields import RichTextField
from django_resized import ResizedImageField


class Type_of_trainer(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название вида тренировки")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = " Вид тренера"
        verbose_name_plural = "Виды  тренеров"


# Create your models here.
class Trainer(models.Model):
    name = models.CharField(max_length=250, verbose_name="Фамилия Имя")
    photo = ResizedImageField(force_format="WEBP", quality=100, upload_to='trainer/', verbose_name="Фотография",blank = True, null = True)
    description = RichTextField(verbose_name="Описание")
    type_of_trainer = models.ForeignKey(Type_of_trainer, on_delete=models.CASCADE, verbose_name="Вид тренера")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тренер"
        verbose_name_plural = "Тренера"
