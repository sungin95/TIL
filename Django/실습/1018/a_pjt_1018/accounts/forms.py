from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ("username", "email")


from django import forms
from .models import profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = profile
        fields = ["profile_image", "content"]
        labels = {
            "content": "상태 메시지",
        }
