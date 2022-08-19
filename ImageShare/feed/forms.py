from django import forms
from django.forms.fields import ImageField
from django.forms.forms import Form
from django.contrib.auth import get_user_model

User = get_user_model()

class PostForm(forms.Form):
    title = forms.CharField(label="Title")
    description = forms.CharField(label="Description")
    author = forms.CharField(label="Creator")
    image = ImageField()


class RegisterForm(forms.Form):
    username = forms.CharField(label='Username')
    email = forms.EmailField(label="Your Email")
    password1 = forms.CharField( label='Enter password',
        widget=forms.PasswordInput(
            attrs={"class":'form-control'}
        )
    )
    password2 = forms.CharField(label='Confirm password',
        widget=forms.PasswordInput(
            attrs={"class":'form-control'}
        )
    )


    def clean_username(self):
        username = self.cleaned_data['username']
        qs = User.objects.filter(username__iexact=username)
        if qs.exists():
            raise forms.ValidationError("This username already exists")

        return username


    def clean_email(self):
        email = self.cleaned_data['email']
        qs = User.objects.filter(email__iexact=email)

        if qs.exists():
            raise forms.ValidationError("This email has already been used")

        return email

class LoginForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(label="password",
    widget=forms.PasswordInput())



    def clean_username(self):
        username = self.cleaned_data['username']
        qs = User.objects.filter(username__iexact=username)
        if not qs.exists():
            raise forms.ValidationError("This user does not exist")

        return username




