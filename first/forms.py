from django import forms

class usersform(forms.Form):
    num1=forms.CharField(label="value 1",required=False,widget=forms.TextInput(attrs={'class':"form-control"}))
    num2=forms.CharField(label="value 2",widget=forms.TextInput(attrs={'class':"form-control"}))
    num3=forms.CharField(label="value 3",widget=forms.TextInput(attrs={'class':"form-control"}))
