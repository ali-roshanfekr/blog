from django import forms
from .models import *


class NewsForm(forms.ModelForm):
    class Meta:
        model = NewsModel
        fields = ('title', 'image', 'author')


class NewsParagraphForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={
        'name': 'title', 'placeholder': 'عنوان'
    }))

    text = forms.CharField(widget=forms.Textarea(attrs={
        'name': 'text', 'placeholder': 'متن'
    }))

    class Meta:
        model = NewsParagraphModel
        fields = ('title', 'text')


class NewsRelatedImageForm(forms.ModelForm):
    class Meta:
        model = NewsRelatedImageModel
        fields = ('image',)
