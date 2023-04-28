from django.contrib import admin
from django.urls import path, include
from django.utils.translation import gettext_lazy as _
from django.views.i18n import set_language
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns



from apps.homepage.views import (
    GeneralHomepageView,
    ReviewsFromCustomersView,
    AboutUsPageView,
    ContactView,
    ContactView,
    ProjectView,
    ArticleView
)




urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('home/', GeneralHomepageView.as_view(), name='home'),
    path('articles/<int:pk>/', ArticleView.as_view(), name='articles'),
    path('about/', AboutUsPageView.as_view(), name='about'),
    path('works/', ProjectView.as_view(), name='works'),
    path('contacts/', ContactView.as_view() , name='contacts'),
    path('contacts/', ContactView.as_view() , name='contacts'),


]

urlpatterns += i18n_patterns(
    path(_('set-language/'), set_language, name='set_language'),

)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    path('home/', GeneralHomepageView.as_view(), name='home'), 
