from django import forms
from .models import *


class RecruitForm(forms.ModelForm):

    class Meta:
        model = Recruit
        exclude = ['is_accepted']


class SithForm(forms.ModelForm):

    #name = forms.ModelMultipleChoiceField(queryset=Sith.objects.all())
    #name = forms.ModelChoiceField(queryset=Sith.objects.all())
    name = forms.BaseModelForm

    class Meta:
        model = Sith
        exclude = ['planet']
