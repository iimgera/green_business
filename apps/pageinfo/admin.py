from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from solo.admin import SingletonModelAdmin
from apps.pageinfo.models import (
    MainPageInfo,
    LinkOfPage,
)



@admin.register(MainPageInfo)
class MainPageInfoAdmin(SingletonModelAdmin, TranslationAdmin):
    list_display = (
            'id',
            'site_name',
            'email',
            'help_text'
            )

@admin.register(LinkOfPage)
class LinkOfPageAdmin(TranslationAdmin, admin.ModelAdmin ):
    list_display = (
            'id',
            'name',
            'link',
            'icon',
            'main_page_info'
            )

