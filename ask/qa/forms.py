__author__ = 'User'
from django import forms
from models import Question, Answer
from django.contrib.auth.models import User

class AskForm(forms.Form):
    title = forms.CharField()
    text = forms.CharField(widget=forms.Textarea)
    def __init__(self, user, **kwargs):
        super(AskForm, self).__init__(**kwargs)
        self._user = user

    def save(self):
        self.cleaned_data['author'] = self._user
        question = Question(**self.cleaned_data)
        question.save()
        return question


class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    question = forms.IntegerField(widget=forms.HiddenInput)
    #def __init__(self, user, **kwargs):
    #    self._user = user
    #    super(AnswerForm, self).__init__(**kwargs)
    def save(self):
    #    self.cleaned_data['author'] = self._user
        answer = Answer(**self.cleaned_data)

        answer.save()
        return answer

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()

class SignupForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
    email = forms.EmailField()
    def save(self):
        user = User(**self.cleaned_data)
        user.save()
        return user