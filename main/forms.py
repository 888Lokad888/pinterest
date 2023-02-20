from django import forms 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from captcha.fields import ReCaptchaField
from .models import *

class AddPostForm(forms.ModelForm):
    captcha = ReCaptchaField()
    class Meta:
        model = Post
        fields = ('photo', 'author', 'tags')
       
class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя')
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(label='Пароль')
    password2 = forms.CharField(label='Подтверждение пароля')
    captcha = ReCaptchaField()

    class Meta:
        model = User 
        fields = ('username', 'email', 'password1', 'password2')

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя')
    password = forms.CharField(label='Пароль')
    captcha = ReCaptchaField()