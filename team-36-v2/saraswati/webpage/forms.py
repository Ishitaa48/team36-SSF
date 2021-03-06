from logging import PlaceHolder
from django import forms

class user(forms.Form):
    choice = [('Select',''),('teacher','Teacher'),('student','Student')]
    register_as = forms.ChoiceField(choices=choice)
    user = forms.CharField(max_length=30, widget=forms.TextInput(attrs={"placeholder":"Username"}))
    email = forms.CharField(max_length=30, widget=forms.EmailInput(attrs={"placeholder":"email"}))
    password = forms.CharField(max_length=30, widget=forms.PasswordInput(attrs={"placeholder":"password"}))
    confirm_password = forms.CharField(max_length=30, widget=forms.PasswordInput(attrs={"placeholder":"confirm_password"}))

class login_user(forms.Form):
    choice = [('Select',''),('teacher','Teacher'),('student','Student')]
    login_as = forms.ChoiceField(choices=choice)
    user = forms.CharField(max_length=30, widget=forms.TextInput(attrs={"placeholder":"Username"}))
    password = forms.CharField(max_length=30, widget=forms.PasswordInput(attrs={"placeholder":"password"}))

class reset_psswrd(forms.Form):
    choice = [('Select',''),('admin','Teacher'),('user','Student')]
    role = forms.ChoiceField(choices=choice)
    user = forms.CharField(max_length=30, widget=forms.TextInput(attrs={"placeholder":"Username"}))
    password = forms.CharField(max_length=30, widget=forms.PasswordInput(attrs={"placeholder":"New password"}))
    conf_password = forms.CharField(max_length=30, widget=forms.PasswordInput(attrs={"placeholder":"Confirm password"}))
