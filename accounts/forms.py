from django.contrib.auth import get_user_model
from django import forms
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from django.forms import fields
from django.forms.models import ModelForm



User = get_user_model()


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self,*args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise ValidationError('usuario incorreto')
            if not user.check_password(password):
                raise ValidationError('senha incorreta')
            if not user.is_active:
                raise ValidationError('usuario desativado')


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        Model = User
        fields = ('username', 'password', 'confirm_password')
    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleanned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        user = User.objects.filter(username=username)
        if user.exists():
            raise ValidationError('usuário ja existe')
        if not password == confirm_password:
            raise ValidationError('password nao confere')
