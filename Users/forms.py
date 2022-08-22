from django import forms
from django.forms import ValidationError
from django.contrib.auth.models import User,auth
from django.contrib.auth.forms import UserCreationForm
class Register(forms.ModelForm):
    username =forms.CharField(label='መጠቀሚያ ስም',help_text='መጠቀሚያ ስሞ ከ 8 ቃላት ማነስ ከ 20 ቃላት መብለጥ የለበትም')
    email = forms.EmailField(label='ኢሜል')
    password1 =forms.CharField(label='የይለፍ ቃል 1',widget=forms.PasswordInput())
    password2 =forms.CharField(label='ማረጋገጫ',widget=forms.PasswordInput())
    class Meta:
        model=User
        fields =['username','email',"password1","password2"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    def clean_email(self):
        email =self.cleaned_data.get("email")
        Email2 =User.objects.filter(email=email).exists()
        if Email2:
            raise ValidationError('ይህ ኢሜል ሌላ አካውንት ተከፍቶበታል')
        return email
    def clean_password2(self):
        password1 =self.cleaned_data.get('password1')
        password2 =self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2 :
            raise ValidationError('ሁለቱ የይለፍ ቃላት አንድ አይደሉም')
        if len(password1) < 8:
            raise ValidationError('የይለፍ ቃል በጣም አጭር ነው')
        if password1.isdigit():
            raise ValidationError('የይለፍ ቃል ሙሉ በሙሉ ቁጥር ሊሆን ይችላል')
        return password2

class LoginForm(forms.Form):
    username = forms.CharField(label='መጠቀሚያ ስሞን',help_text='ሲመዘገቡ የተጠቀሙትን መጠቀሚያ ስም ያስገቡ፡፡')
    password = forms.CharField(label='ማለፊያ ቃሎን',widget=forms.PasswordInput(),help_text='ሲመዘገቡ የተጠቀሙትን ማለፊያ ቃል ያስገቡ፡፡')

    def clean_username(self):
        username = self.cleaned_data.get('username')
        r =User.objects.filter(username=username)
        if not r.count():
            raise ValidationError("ይሄ መጠቀሚያ ስም አልተፈጠረም")
        return username
    def clean_password(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        aut =auth.authenticate(username=username, password=password)
        if aut is None:
            raise ValidationError('ማለፊያ ቃሉን ማረጋገጥ አልተቻለም')
        return password
    def checkVerf(self):
        username=self.cleaned_data.get('username')
        if User.objects.filter(username=username):
            ver = User.objects.filter(username=username).first()
            if ver.is_active == False:
                raise ValidationError('ኣካውንቶ አልተረጋገጠም ያረጋግጡ')
            return ver
        else:
            return 0
