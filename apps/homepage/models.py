from django.db import models

from solo.models import SingletonModel

from ckeditor.fields import RichTextField


class GeneralMainPage(SingletonModel):
    title = models.CharField(
        max_length=150,
        verbose_name='Заголовок'
    )
    sub_title = models.CharField(
        max_length=150,
        verbose_name='Подзаголовок'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Общая основная страница'
        ordering = ['-id']


class Project(SingletonModel):
    title = models.CharField(
        max_length=150,
        verbose_name='Заголовок'
    )
    description = RichTextField(
        verbose_name='Описание'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Вкладка "Projects'
        ordering = ['-id']

class Feedback(SingletonModel):
    title=models.CharField(
        max_length=150,
        verbose_name='Заголовок'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Что-то под Наши работы'
        ordering = ['-id']


class AboutUs(SingletonModel):
    title = models.CharField(
        max_length=150,
        verbose_name='Заголовок'
    )
    description = RichTextField(
        verbose_name='Описание',
        help_text='Enter your content here.'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'
        ordering = ['-id']


class Contact(SingletonModel):
    title = models.CharField(
        max_length=150,
        verbose_name='Заголовок'
    )
    description = models.TextField(
        verbose_name='Описание'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Контакты'
        ordering = ['-id']




