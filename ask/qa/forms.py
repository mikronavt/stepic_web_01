__author__ = 'User'
from django import forms
from models import Question, Answer

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

#class LoginForm(forms.Form):

class SignupForm(forms.Form):
    login = forms.CharField()
    password = forms.PasswordInput()
    email = forms.EmailField()
