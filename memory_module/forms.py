from django import forms
from .models import *


class MemoryForm(forms.ModelForm):
    class Meta:
        model = MemoryModel
        fields = ('title', 'image', 'author')


class MemoryParagraphForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={
        'name': 'title', 'placeholder': 'عنوان'
    }))

    text = forms.CharField(widget=forms.Textarea(attrs={
        'name': 'text', 'placeholder': 'متن'
    }))

    quote = forms.CharField(widget=forms.Textarea(attrs={
        'name': 'quote', 'placeholder': 'نقل قول'
    }))

    class Meta:
        model = MemoryParagraphModel
        fields = ('title', 'text', 'quote')


class MemoryRelatedImageForm(forms.ModelForm):
    class Meta:
        model = MemoryRelatedImageModel
        fields = ('image',)