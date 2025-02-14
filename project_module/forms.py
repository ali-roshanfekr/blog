from django import forms
from .models import *


class ProjectForm(forms.ModelForm):
    class Meta:
        model = ProjectModel
        fields = ('title', 'image', 'tag')


class ProjectParagraphForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={
        'name': 'title', 'placeholder': 'عنوان'
    }))

    text = forms.CharField(widget=forms.Textarea(attrs={
        'name': 'text', 'placeholder': 'متن'
    }))

    class Meta:
        model = ParagraphModel
        fields = ('title', 'text')


class ProjectRelatedImageForm(forms.ModelForm):
    class Meta:
        model = RelatedImageModel
        fields = ('image',)
