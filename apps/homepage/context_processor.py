import requests
from apps.articles.models import (
    Article,
    Review
)
from apps.homepage.models import (
    GeneralMainPage, 
    Contact,
    AboutUs,
    Project,
    Feedback
)
from apps.pageinfo.models import (
    MainPageInfo,
    LinkOfPage
)


def general(request):
    return {'general': GeneralMainPage.objects.first()}

def page_info(request):
    return {'page_info': MainPageInfo.objects.first()}

def subproject(request):
    return {'subproject': LinkOfPage.objects.all()}

def articles(request):
    return {'articles': Article.objects.all()}

def about(request):
    return {'about': AboutUs.objects.all()}

def work(request):
    return {'works': Project.objects.first()}

def feedback(request):
    return {'feedbacks': Feedback.objects.first()}

def general_main_title(request):
    return {'general_main_title': GeneralMainPage.objects.first()}

def reviews(request):
    return {'reviews': Review.objects.all()}

def contacts(request):
    return {'contacts': Contact.objects.all()}

def contact(request):
    return {'contact': Contact.objects.all()}

def article_detail(request):
    return {'article_detail': Article.objects.all()}