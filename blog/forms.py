from django import forms

from .models import Post, PostImage


class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description', 'slug']


class PostModelFormImage(forms.ModelForm):
    class Meta:
        model = PostImage
        fields = ['title', 'image']