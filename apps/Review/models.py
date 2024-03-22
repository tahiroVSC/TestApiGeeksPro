from django.db import models
from ckeditor.fields import RichTextField
from django_resized import ResizedImageField


class Review(models.Model):
    photo = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='photo/',
        verbose_name="Фотография",
        blank = True, null = True
    )
    name = models.CharField(
        max_length=255,
        verbose_name="ФИО"
    )
    jobtitle = models.CharField(
        max_length = 255,
        verbose_name = "Должность"
    )
    description = RichTextField(
        verbose_name="Отзыв"
    )
    created = models.DateField(
        auto_now=True,
        verbose_name="Дата публикации"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
