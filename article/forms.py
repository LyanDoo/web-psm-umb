from django import forms
from .models import Article
from ckeditor.fields import RichTextField

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title','body']
        widgets = {
            'title' : forms.TextInput(),
            'body' : RichTextField()
        }