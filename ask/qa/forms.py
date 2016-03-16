__author__ = 'User'
from django import forms
from models import Question, Answer, User

class AskForm(forms.Form):
    title = forms.CharField()
    text = forms.CharField(widget=forms.Textarea)

    def save(self):
        question = Question(**self.cleaned_data)
        question.save()
        return question


class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    question = forms.IntegerField(widget=forms.HiddenInput)
    def save(self):
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