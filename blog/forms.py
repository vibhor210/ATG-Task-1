from django import forms
from blog.models import blog

class BlogForm(forms.ModelForm):
    class Meta:
        model = blog
        fields = ("title","image","draft","category","summary","content")