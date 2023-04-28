from django import forms
from apps.articles.models import Review
from django.core.exceptions import ValidationError
from django.core.validators import validate_email


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = (
            'author',
            'email',
            'review',
            'image',
            'article',
    )
    
    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            validate_email(email)
        except ValidationError:
            raise forms.ValidationError('Неверный формат электронной почты.')
        return email