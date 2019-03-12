from django import forms
from superIndex.models import Customer
from django.contrib.auth.models import User

class User_Form(forms.ModelForm):
    password =  forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ("username","email","password")

class Customer_Form(forms.ModelForm):
    sex = (('M','Male'),
            ('F','Female')
    )
    gender = forms.ChoiceField(choices=sex)
    class Meta():
        model = Customer
        fields = ("cust_id","cust_name",'address','gender','govt_proof','contact_num')
