from django import forms
from .models import Article, Comment


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["title", "content", "thumbnail"]
        labels = {
            "title": "제목",
            "content": "내용",
            "thumbnail": "사진",
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            "content",
        ]
        labels = {
            "content": "댓글쓰기",
        }
