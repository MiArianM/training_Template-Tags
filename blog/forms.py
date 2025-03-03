from django import forms


class Ticketform(forms.Form):
    subject_choices = (('فنی', 'فنی'), ('باگ', 'باگ'), ('ایده', 'ایده'))
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    to = forms.EmailField()
    subject = forms.ChoiceField(choices=subject_choices)
    comment = forms.CharField(required=False, widget=forms.Textarea)
