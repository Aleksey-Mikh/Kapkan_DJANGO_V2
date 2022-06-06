from django import forms
from .models import Order
from captcha.fields import CaptchaField


class OrderCreateForm(forms.ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = Order
        fields = ('first_name', 'last_name', 'middle_name', 'email', 'address', 'phone', 'comment_for_order')
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'my-field-form'}),
            'last_name': forms.TextInput(attrs={'class': 'my-field-form'}),
            'middle_name': forms.TextInput(attrs={'class': 'my-field-form'}),
            'email': forms.TextInput(attrs={'class': 'my-field-form'}),
            'address': forms.TextInput(attrs={'class': 'my-field-form'}),
            'phone': forms.TextInput(attrs={'class': 'my-field-form'}),
            'comment_for_order': forms.Textarea(attrs={'class': 'my-field-form comment'}),
        }
