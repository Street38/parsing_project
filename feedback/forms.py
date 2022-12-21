from django import forms
from .models import FeedbackModel
from phonenumber_field.formfields import PhoneNumberField


class FeedbackForms(forms.ModelForm):
    name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone_number = PhoneNumberField(label='Номер телефона(Если нужен ответ)', required=False,
                                    widget=forms.TextInput(attrs={'class': 'form-control'}))
    # email = forms.EmailField(label='Почта', required=False, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    message = forms.CharField(label='Текст сообщения', widget=forms.Textarea(attrs={'class': 'form-control'}))

    class Meta:
        model = FeedbackModel
        fields = ['name', 'phone_number', 'message']

    phone_number.error_messages['invalid'] = \
        'В формате +79001111111'  # Изменяем словарь с ошибками для поля номер телефона
