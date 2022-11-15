from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User


# Create your models here.
class LoginForm(forms.Form):
    username = forms.CharField()
    password =forms.CharField()

class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username','email')

   
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            print('password error')
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )
        return confirm_password

     

  