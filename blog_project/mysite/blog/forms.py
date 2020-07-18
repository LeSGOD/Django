from django import forms
from blog.models import Post, Comment


class PostForm(forms.ModelForm):
    """Form definition for Post."""

    class Meta:
        """Meta definition for Postform."""

        model = Post
        fields = ('author', 'text', 'title')

    widgets = {
        'title': forms.TextInput(attrs={'class': 'textinputclass'})
        'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'})
    }


class CommentForm(forms.ModelForm):
    """Form definition for Comment."""

    class Meta:
        """Meta definition for Commentform."""

        model = Comment
        fields = ('author', 'text')

        widgets = {
            'author': forms.TextInput(attrs={'class': 'textinputclass'})
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'})
        }
