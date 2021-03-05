from django import forms
from .models import Order
from captcha.fields import CaptchaField
from django.contrib.auth.models import User


class OrderCreateForm(forms.ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address','phone', 'comment_for_order']