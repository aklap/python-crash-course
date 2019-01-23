from django.forms import ModelForm, Textarea

from .models import BlogPost


class BlogPostForm(ModelForm):
    class Meta:
        model = BlogPost
        # Fields are text fields by default
        fields = ['title', 'text']
        labels = {'text': ''}
        # Overwrite text being a textfield
        widgets = {'text': Textarea(attrs={'cols': 80})}
