from django import forms
from .models import Message

class MessageForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'ct-controll', 'placeholder': 'Ваше Имя'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'ct-controll', 'placeholder': 'Ваш Телефон'}))
    city = forms.CharField(widget=forms.TextInput(attrs={'class': 'ct-controll', 'placeholder': 'Город'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'ct-controll', 'placeholder': 'Email'}))
    text_message = forms.CharField(widget=forms.Textarea(attrs={'class': 'ct-controll', 'placeholder': 'Сообщение','rows':2,}))
    class Meta:
        model = Message
        fields = ('name', 'phone', 'city', 'email', 'text_message')


