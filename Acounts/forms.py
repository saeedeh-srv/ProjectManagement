from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.forms import AuthenticationForm
from django import forms


class UserRegisterForm(forms.ModelForm):
    username = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                                            'id': 'form3Example1'}))
    first_name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                                              'id': 'form3Example3'}))
    last_name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                                             'id': 'form3Example4'}))
    password_1 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                                   'id': 'form3Example5',
                                                                                   'type': 'password', }))
    email = forms.EmailField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                           'id': 'form3Example2'}))
    phone_number = forms.CharField(required=True, max_length=12, widget=forms.TextInput(
        attrs={'class': 'form-control', 'id': 'form3Example7', 'name': 'phone_number'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', ]

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("This user is exist now choose something else")
        return username

    def clean_password_1(self):
        password1 = self.cleaned_data["password_1"]
        if len(password1) < 8:
            raise forms.ValidationError("password is too short you should choose more than 8 characters")
        return password1

    def clean_phone_number(self):
        phone_number = self.cleaned_data["phone_number"]
        if Profile.objects.filter(phone=phone_number).exists():
            raise forms.ValidationError("this phone_number was taken")
        return phone_number


class UserLoginForm(AuthenticationForm):
    password = forms.CharField(max_length=100, required=True,
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'form3Example4'}))
    remember = forms.BooleanField(required=False, widget=forms.CheckboxInput(
        attrs={'class': 'form-check-input me-2', 'id': 'form2Example33'}))
    username = forms.CharField(max_length=100, required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'form3Example1'}))

    def __init__(self, *args, **kwargs):
        self.error_messages['invalid_login'] = 'username or password is incorect'
        super().__init__(*args, **kwargs)


class UserprofileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
