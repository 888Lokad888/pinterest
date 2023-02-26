from django import forms 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
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
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput())
    captcha = ReCaptchaField()

    class Meta:
        model = User 
        fields = ('username', 'password1', 'password2')

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput())
    captcha = ReCaptchaField()

class ProfileForm(UserChangeForm):
    class Meta:
        model = User 
        fields = ('username',)

class UpdateProfileForm(forms.ModelForm):
    avatar = forms.ImageField(widget=forms.FileInput())
    class Meta:
        model = UserProfile
        fields = ('avatar',)

class CommentsForm(forms.ModelForm):
    content = forms.CharField(label='Комментарии', widget=forms.Textarea(attrs={
            'rows': 4,
            'placeholder': 'Написать комментарий...'
        }))
    class Meta:
        model = Comments
        fields = ('content',)