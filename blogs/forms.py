from django import forms
from blogs.models import Comment, Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'overview', 'categories']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']