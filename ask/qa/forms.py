#coding: utf-8
from django import forms

from qa.models import Question, Answer


class AskForm(forms.Form):
    title = forms.CharField(max_length=255)
    title.widget.attrs['class'] = 'form-control'
    text = forms.CharField(widget=forms.Textarea)
    text.widget.attrs['class'] = 'form-control'
    def save(self):
        print self._user
        self.cleaned_data['author_id'] = self._user.id
        return Question.objects.create(**self.cleaned_data)


class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    text.widget.attrs['class'] = 'form-control'
    question = forms.IntegerField(widget=forms.HiddenInput)
    def clean_question(self):
        question = self.cleaned_data.get('question')
        if question and Question.objects.filter(pk=question).exists():
            return Question.objects.filter(pk=question)[0]
        raise forms.ValidationError(u'Not id question', code=12)
    def save(self):
        self.cleaned_data['author_id'] = self._user.id
        return Answer.objects.create(**self.cleaned_data)


