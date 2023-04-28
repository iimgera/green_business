from modeltranslation.translator import (
    translator, 
    TranslationOptions
)
from apps.pageinfo.models import (
    MainPageInfo,
    LinkOfPage
)
from apps.homepage.models import (
    GeneralMainPage, 
    Project,
    Feedback,
    AboutUs, 
    Contact
)
from apps.articles.models import (
    Article,
    Review
)


class LinkOfPageTranslationOptions(TranslationOptions):
    fields = (
        'name', 
        'main_page_info'
    )
translator.register(LinkOfPage, LinkOfPageTranslationOptions)


class MainPageInfoTranslationOptions(TranslationOptions):
    fields = (
        'site_name',
        'help_text'
    )
translator.register(MainPageInfo, MainPageInfoTranslationOptions)


class GeneralMainPageTranslationOptions(TranslationOptions):
    fields = (
        'title', 
        'sub_title'
    )
translator.register(GeneralMainPage, GeneralMainPageTranslationOptions)


class AboutUsTranslationOptions(TranslationOptions):
    fields = (
        'title', 
        'description'
    )
translator.register(AboutUs, AboutUsTranslationOptions)


class ProjectTranslationOptions(TranslationOptions):
    fields = (
        'title', 
        'description'
    )
translator.register(Project, ProjectTranslationOptions)


class FeedbackTranslationOptions(TranslationOptions):
    fields = (
        'title', 
    )
translator.register(Feedback, FeedbackTranslationOptions)


class ContactTranslationOptions(TranslationOptions):
    fields = (
        'title', 
        'description'
    )
translator.register(Contact, ContactTranslationOptions)


class ArticleTranslationOptions(TranslationOptions):
    fields = (
        'title', 
        'description', 
        'project_info'
    )
translator.register(Article, ArticleTranslationOptions)


class ReviewTranslationOptions(TranslationOptions):
    fields = (
        'author', 
        'review', 
        'article'
    )
translator.register( Review, ReviewTranslationOptions)
