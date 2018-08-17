from django import forms

from .models import Books

class BookForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = [
            'user',
            'author',
            'content',
            'image'
        ]

    def clean_content(self, *args, **kwargs):
        #requires data to be less than 240 characters
        content = self.cleaned_data.get('content')
        if len(content) > 240:
            raise forms.ValidationError("Content is too long")
        return content

    def clean(self, *args, **kwargs):
        #makes it so cannot create empty posts
        data = self.cleaned_data
        content = data.get('content', None)
        if content == "":
            content = None
        image = data.get("image", None)
        if content is None and image is None:
            raise forms.ValidationError('Content or image is required.')
        return super().clean(*args, **kwargs)

