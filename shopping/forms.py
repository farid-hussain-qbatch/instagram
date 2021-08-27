from shopping.models import Customer
from django import forms

class CreatecustomerForm(forms.Form):
    customer_name = forms.CharField(label='customer_name', max_length=100)
    customer_phone = forms.CharField(label='customer_phone', max_length=100)
    customer_address = forms.CharField(label='customer_address', max_length=100)
    supermart_id = forms.CharField(label='supermart_id', max_length=100)
    
    