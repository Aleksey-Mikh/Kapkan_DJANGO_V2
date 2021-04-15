from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from captcha.fields import CaptchaField

from .models import Profile, CustomUser


class UserEditForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'middle_name', 'email', 'phone')
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'my-field-form'}),
            'last_name': forms.TextInput(attrs={'class': 'my-field-form'}),
            'middle_name': forms.TextInput(attrs={'class': 'my-field-form'}),
            'email': forms.TextInput(attrs={'class': 'my-field-form'}),
            'phone': forms.TextInput(attrs={'class': 'my-field-form'}),
        }


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(
        attrs={'class': 'my-field-form'}
    ))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(
        attrs={'class': 'my-field-form'}
    ))
    captcha = CaptchaField()

    error_css_class = "error"


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(
        attrs={'class': 'my-field-form'}
    ))
    first_name = forms.CharField(label='Имя', widget=forms.TextInput(
        attrs={'class': 'my-field-form'}
    ))
    last_name = forms.CharField(label='Фамилия', widget=forms.TextInput(
        attrs={'class': 'my-field-form'}
    ))
    middle_name = forms.CharField(label='Отчество', widget=forms.TextInput(
        attrs={'class': 'my-field-form'}
    ))
    email = forms.EmailField(label='E-mail', widget=forms.TextInput(
        attrs={'class': 'my-field-form'}
    ))
    phone = forms.CharField(label='Номер телефона', widget=forms.TextInput(
        attrs={'class': 'my-field-form'}
    ))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(
        attrs={'class': 'my-field-form'}
    ))
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput(
        attrs={'class': 'my-field-form'}
    ))
    captcha = CaptchaField()

    error_css_class = "error"

    class Meta:
        model = CustomUser
        fields = (
            'username',
            'first_name',
            'last_name',
            'middle_name',
            'email',
            'phone',
            'password1',
            'password2',
        )

