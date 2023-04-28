import requests
import telegram
import io
from PIL import Image

from django.shortcuts import (
    render, 
    redirect,
    reverse
)
from django.views.generic import (
    TemplateView,
    FormView
)
from apps.homepage.forms import (
    ReviewForm
)
from apps.articles.models import (
    Review,
    Article,
    TelegramBotSettings
)
from apps.homepage.sender import (
    send_message
)



class GeneralHomepageView(TemplateView):
    template_name = 'homepage/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context.update({})
        return context


class AboutUsPageView(TemplateView):
    template_name = 'homepage/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context.update({})
        return context

class MainPageInfoView(TemplateView):
    template_name = 'homepage/base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context.update({})
        return context

class ProjectView(TemplateView):
    template_name = 'homepage/work.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context.update({})
        return context


class FeedbackView(TemplateView):
    template_name = 'homepage/work.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context.update({})
        return context


class ReviewsFromCustomersView(TemplateView):
    template_name = 'homepage/work.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context.update({
            'reviews': Review.objects.filter(is_active=True),
        })
        return context


class ContactView(TemplateView):
    template_name = 'homepage/contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context.update({})
        return context

class ContactView(FormView):
    template_name = 'homepage/contact.html'
    form_class = ReviewForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context.update({})
        return context
    
    def get(self, request, *args, **kwargs):
        data = request.GET
        return super().get(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('contacts')

    def form_valid(self, form):
        form.save()
        telegram_settings = TelegramBotSettings.objects.first()
        chat_id = telegram_settings.channel_chat_id
        image_path = form.instance.image.path
        with open(image_path, 'rb') as f:
            response = requests.post(
                f"https://api.telegram.org/bot{telegram_settings.bot_token}/sendPhoto",
                data={
                    "chat_id": chat_id,
                },
                files={
                    "photo": f,
                },
            )

        if not response.ok:
            response.raise_for_status()

        message = f"Новый отзыв от {form.instance.author}:\n" \
                f"Эл. почта: {form.instance.email}\n" \
                f"Сообщение: {form.instance.review}\n" \
                f"К статье: {form.instance.article}"
        send_message(message, chat_id)
        return super().form_valid(form)


class SubprojectView(TemplateView):
    template_name = 'homepage/subproject.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context.update({})
        return context



class ArticleView(TemplateView):
    template_name = 'homepage/project.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context.update({})
        return context