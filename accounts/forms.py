from django import forms
from .models import *

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer','product','status']


class customerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['user']
