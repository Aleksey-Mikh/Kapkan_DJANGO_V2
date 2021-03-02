from django import forms
from .models import Order
from captcha.fields import CaptchaField


class OrderCreateForm(forms.ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'city', 'comment_for_order']