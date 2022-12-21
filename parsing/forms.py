from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import TrackingModel, PersonalAccount



class SignupForm(UserCreationForm):
    username = forms.CharField(label='Логин',
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'От 3 символов'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'От 8 символов. Цифры, ниж. и верх. регистр'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Логин',
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Логин'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Пароль'}))

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class CreateTrackingForm(forms.ModelForm):
    description = forms.CharField(label='Описание',
                                  widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Кроссовки найк'}))
    linkproduct = forms.URLField(label='Ссылка на товар', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'https://www.wildberries.ru/'}))
    price = forms.FloatField(label='Цена',
                             widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '1000'}))

    class Meta:
        model = TrackingModel
        fields = ['description', 'linkproduct', 'price']



class UpdateTrackingForm(forms.ModelForm):
    description = forms.CharField(label='Описание',
                                  widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Кроссовки'}))
    linkproduct = forms.URLField(label='Ссылка на товар', widget=forms.URLInput(
        attrs={'class': 'form-control', 'placeholder': 'https://www.wildberries.ru/'}))
    price = forms.FloatField(label='Цена',
                             widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '1000'}))
    complete = forms.BooleanField(label='Завершить отслеживание', required=False)

    class Meta:
        model = TrackingModel
        fields = ['description', 'linkproduct', 'price', 'complete']



class ArchiveTrackingForm(forms.ModelForm):
    description = forms.CharField(label='Описание',
                                  widget=forms.TextInput(attrs={'class': 'form-control'}))
    linkproduct = forms.URLField(label='Ссылка на товар', widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    price = forms.FloatField(label='Цена',
                             widget=forms.TextInput(attrs={'class': 'form-control'}))
    datecomplite = forms.DateTimeField(label='Дата завершения',
                                       widget=forms.DateTimeInput(attrs={'class': 'form-control'}))

    class Meta:
        model = TrackingModel
        fields = ['description', 'linkproduct', 'price', 'datecomplite']


class PersonalForms(forms.ModelForm):
    name = forms.CharField(label='Имя',
                           widget=forms.TextInput(attrs={'class': 'form-control', 'readonly':'readonly'}))
    telegram_account = forms.CharField(label='Телеграм',
                           widget=forms.TextInput(attrs={'class': 'form-control', 'readonly':'readonly'}))

    class Meta:
        model = PersonalAccount
        fields = ['name', 'telegram_account']


# class FeedbackForms(forms.Form):
#     name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'form-control'}))
#     # phone_number = PhoneNumberField()
#     email = forms.EmailField(label='Почта', widget=forms.EmailInput(attrs={'class': 'form-control'}))
#     message = forms.CharField(label='Текст сообщения', widget=forms.Textarea(attrs={'class': 'form-control'}))