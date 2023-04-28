from django.db import models
from solo.models import SingletonModel


class MainPageInfo(SingletonModel):
    site_name = models.CharField(
        max_length=50,
        verbose_name='Название сайта'
    )
    email = models.EmailField(
        verbose_name='Почта'
    )
    help_text = models.CharField(
        verbose_name='Хэлпер текст', 
        max_length=100
    )

    def __str__(self):
        return self.site_name

    class Meta:
        verbose_name = 'Сайт'
        verbose_name_plural = 'Сайты'


class LinkOfPage(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name='Название'
    )
    link = models.URLField(
        verbose_name='Ссылка'
    )
    icon = models.FileField(
        verbose_name='Иконка', 
        upload_to='%Y/%m/%d/'
    )
    main_page_info = models.ForeignKey(
        MainPageInfo,
        on_delete=models.CASCADE,
        related_name='links',
        verbose_name='Информация о сайте'
    )

    def __str__(self):
        return self.name
        
    class Meta:
        verbose_name = 'Ссылка'
        verbose_name_plural = 'Ссылки'

