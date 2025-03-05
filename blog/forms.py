from django import forms
from .models import POST


class Ticketform(forms.Form):
    title = forms.CharField()
    description = forms.CharField()
    subject_choices = (('فنی', 'فنی'), ('باگ', 'باگ'), ('ایده', 'ایده'))
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    to = forms.EmailField()
    subject = forms.ChoiceField(choices=subject_choices)
    comment = forms.CharField(required=False, widget=forms.Textarea)


class Postform(forms.ModelForm):
    class Meta:
        model = POST
        fields = ('title', 'content', 'slug', 'reading_time')

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 4:
            raise forms.ValidationError('Please enter a title of at least 4 characters')
        return title  # مقدار معتبر برگردانده می‌شود

    def clean_content(self):
        content = self.cleaned_data.get('content')
        if len(content) < 8:
            raise forms.ValidationError('Please enter content of at least 8 characters')
        return content

    def clean_slug(self):
        slug = self.cleaned_data.get('slug')
        if "_" in slug:
            raise forms.ValidationError('Please enter valid characters, "_" is not allowed')
        return slug

    def clean_rt(self):
        rt = self.cleaned_data.get('reading_time')
        if type(rt) is not int:
            raise forms.ValidationError('Please enter valid time')
        return rt
