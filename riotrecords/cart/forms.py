from django import forms


class OrderForm(forms.Form):
    address = forms.CharField()