from django import forms
from django.forms import ValidationError
from django.contrib.auth.models import User,auth
from django.contrib.auth.forms import UserCreationForm
class Register(forms.ModelForm):
    username =forms.CharField(label='Username',help_text='username shouldn\'t be less than 8 characters or exceed 20 character')
    email = forms.EmailField(label='Email')
    password1 =forms.CharField(label='Password',widget=forms.PasswordInput())
    password2 =forms.CharField(label='Confirm Password',widget=forms.PasswordInput())
    class Meta:
        model=User
        fields =['username','email',"password1","password2"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    def clean_email(self):
        email =self.cleaned_data.get("email")
        Email2 =User.objects.filter(email=email).exists()
        if Email2:
            raise ValidationError('this username is taken')
        return email
    def clean_password2(self):
        password1 =self.cleaned_data.get('password1')
        password2 =self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2 :
            raise ValidationError('the two passwords don\'t match')
        if len(password1) < 8:
            raise ValidationError('password to short')
        if password1.isdigit():
            raise ValidationError('password can\'t be all number')
        return password2

class LoginForm(forms.Form):
    username =forms.CharField(label='Username',help_text='enter the username you used to sign up')
    password = forms.CharField(label='Password',widget=forms.PasswordInput(),help_text='enter the password you used to sign up')

    def clean_username(self):
        username = self.cleaned_data.get('username')
        r =User.objects.filter(username=username)
        if not r.count():
            raise ValidationError("this username is not registered")
        return username
    def clean_password(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        aut =auth.authenticate(username=username, password=password)
        if aut is None:
            raise ValidationError('can\'t verfy your password')
        return password
    def checkVerf(self):
        username=self.cleaned_data.get('username')
        if User.objects.filter(username=username):
            ver = User.objects.filter(username=username).first()
            if ver.is_active == False:
                raise ValidationError('please verify your account')
            return ver
        else:
            return 0
