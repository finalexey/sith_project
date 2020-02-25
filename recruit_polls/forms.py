# from django import forms
# from .models import *
#
#
# class QuestionForm(forms.ModelForm):
#
#     question = forms.ModelMultipleChoiceField(queryset=Question.objects.all())
#
#     class Meta:
#         model = Question
#         exclude = ['']
#
#
# class AnswerForm(forms.ModelForm):
#
#     class Meta:
#         model = Answer
#         exclude = ['']
#
#
# class PollForm(forms.ModelForm):
#
#     #question = forms.ModelMultipleChoiceField(queryset=Question.objects.all())
#     question = list(Question.objects.all())
#
#     class Meta:
#         model = Poll
#         exclude = ['recruit']
