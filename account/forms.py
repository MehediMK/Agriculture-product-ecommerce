from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import User_info


class UserSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ('first_name','last_name','username','email')

class UserInfo(forms.ModelForm):
    # user = forms.CharField(widget=forms.TextInput(attrs={'type':'hidden'}))
    class Meta:
        model = User_info
        fields = ('profile_pic','gender','address','phone')


class UserFLEname(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name','last_name','email')