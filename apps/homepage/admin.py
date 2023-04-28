from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from solo.admin import SingletonModelAdmin
from apps.homepage.models import (
    GeneralMainPage,
    Project,
    Feedback,
    AboutUs,
    Contact
    )



@admin.register(GeneralMainPage)
class GeneralMainPageAdmin(SingletonModelAdmin, TranslationAdmin):
    list_display = (
            'id',
            'title',
            'sub_title',
            )

@admin.register(Project)
class ProjectAdmin(SingletonModelAdmin, TranslationAdmin):
    list_display = (
            'id',
            'title',
            'description',
            )

@admin.register(Feedback)
class FeedbackAdmin(SingletonModelAdmin, TranslationAdmin):
    list_display = (
            'id',
            'title',
            )

@admin.register(AboutUs)
class AboutUsAdmin(SingletonModelAdmin, TranslationAdmin):
    list_display = (
            'id',
            'title',
            'description',
            )

@admin.register(Contact)
class Contact(SingletonModelAdmin, TranslationAdmin):
    list_display = (
            'id',
            'title',
            'description',
            )
