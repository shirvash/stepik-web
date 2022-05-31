from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User

from .models import Question, Answer


class AskForm(ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'text']

    def save(self):
        _title = self.cleaned_data['title']
        _text = self.cleaned_data['text']
        qu = Question(title=_title, text=_text)
        #qu.author_id = self._user
        qu.save()
        return qu


class AnswerForm(ModelForm):
    class Meta:
        model = Answer
        fields = ['text', 'question']
        widgets = {'question': forms.HiddenInput()}

    def clean_question(self):
        _qu = self.cleaned_data['question']
        try:
            qu = Question.objects.get(pk=_qu.id)
        except:
            raise forms.ValidationError('question does not exist')
        else:
            return qu

    def save(self):
        _text = self.cleaned_data['text']
        _question = self.cleaned_data['question']
        ask = Answer(text=_text, question=_question)
        #ask.author_id = self._user
        ask.save()
        return ask


#class LoginForm(ModelForm):
    # class Meta:
    #     model = User
    #     fields = ['username', 'password']
    #     widgets = {'password': forms.PasswordInput()}
    #
    # def clean(self):
    #     username = self.cleaned_data['username']
    #     password = self.cleaned_data['password']
    #     try:
    #         user = User.objects.get(username=username)
    #     except User.DoesNotExist:
    #         raise forms.ValidationError('wrong username or password')
    #     else:
    #         return user


# class SignupForm(ModelForm):
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password']
#
#     def save(self):
#         _un = self.cleaned_data['username']
#         _pw = self.cleaned_data['password']
#         _em = self.cleaned_data['email']
#         user = User.objects.create_user(_un, _em, _pw)
#         return user