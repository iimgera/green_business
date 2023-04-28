from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from apps.articles.models import (
    Article,
    Review,
    TelegramBotSettings
)



@admin.register(Article)
class ArticleAdmin(TranslationAdmin, admin.ModelAdmin):
    list_display = (
            'id',
            'title',
            'description',
            'image',
            'project_info'
    )

@admin.register(Review)
class ReviewAdmin(TranslationAdmin, admin.ModelAdmin):
    list_display = (
            'id',
            'author',
            'email',
            'review',
            'image',
            'is_active',
            'article'
    )

@admin.register(TelegramBotSettings)
class TelegramBotSettingsAdmin(admin.ModelAdmin):
    list_display = (
            'id',
            'bot_token',
            'channel_chat_id'   
    )