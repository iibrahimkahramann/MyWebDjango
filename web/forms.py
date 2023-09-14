from django import forms
from .models import Contact


class ContactForms(forms.ModelForm):
    class Meta:
        model = Contact
        exclude = ('iletişim',)
        fields = ['name_surname', 'email', 'mesaj']
        labels = {
            'name_surname': 'İsim Soyisim',
            'email': 'E-posta',
            'mesaj': 'Mesaj'
        }



