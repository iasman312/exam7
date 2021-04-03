from django import forms

from mainapp.models import Poll


class PollForm(forms.ModelForm):
    class Meta:
        model = Poll
        fields = ('question',)
