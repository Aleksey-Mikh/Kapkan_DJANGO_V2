from django import forms


class ProductFilterForm(forms.Form):
    min_price = forms.IntegerField(label="from", required=False, widget=forms.TextInput(
        attrs={'class': 'my-field-form'}))
    max_price = forms.IntegerField(label="to", required=False, widget=forms.TextInput(
        attrs={'class': 'my-field-form'}))
    is_new = forms.BooleanField(label='NEW', required=False)
    is_hit = forms.BooleanField(label='ХИТ', required=False)
    is_recommend = forms.BooleanField(label='Рекомендованно', required=False)