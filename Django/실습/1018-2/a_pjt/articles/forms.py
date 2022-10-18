from django import forms
from .models import Article

from .models import CommentA


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["title", "content"]
        labels = {
            "title": "제목",
            "content": "내용",
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentA
        fields = ["content"]
        labels = {
            "content": "댓글",
        }
