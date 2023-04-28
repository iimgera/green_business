from django.db import models

from ckeditor.fields import RichTextField
from solo.models import SingletonModel



class Article(models.Model):
    title = models.CharField(
        max_length=150,
        verbose_name='Заголовок'
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    image = models.ImageField(
        upload_to='articles/%Y/%m/%d/',
        verbose_name='Изображения'
    )
    project_info = RichTextField(
        verbose_name='Информация о проекте'
    )

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title


class Review(models.Model):
    author = models.CharField(
        max_length=15,
        verbose_name='Автор'
    )
    email = models.EmailField(
        verbose_name='Почта'
    )
    review = models.TextField(
        verbose_name='Отзыв',
        null=True,
        blank=True,
    )
    image = models.ImageField(
        verbose_name='Изображения',
        upload_to='reviews/%Y/%m/%d/'
    )
    is_active = models.BooleanField(
        default=False,
        verbose_name='Статус'
    )
    article = models.ForeignKey(
        Article,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='reviews'
    )

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return self.author


class TelegramBotSettings(models.Model):
    bot_token = models.CharField(max_length=200)
    channel_chat_id = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Telegram Bot Settings'
        verbose_name_plural = 'Telegram Bot Settings'

    def __str__(self):
        return f'Telegram Bot Settings ({self.bot_token})'
