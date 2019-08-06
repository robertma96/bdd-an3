from django import forms
from django.forms import ModelForm
from .models import Pacient, Medic, Medicament, Consultatie
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import datetime


class MedicForm(ModelForm):
    class Meta:
        model = Medic
        fields = ('numemedic', 'prenumemedic', 'specializare')
        widgets = {
            'numemedic': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Introduceti numele'}),
            'prenumemedic': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Introduceti prenumele'}),
            'specializare': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Introduceti specializarea'}),
        }
        labels = {
            'numemedic': 'Nume',
            'prenumemedic': 'Prenume',
            'specializare': 'Specializare'
        }


class PacientForm(ModelForm):
    class Meta:
        model = Pacient
        fields = ('cnp', 'numepacient', 'prenumepacient', 'adresa', 'asigurare',)
        widgets = {
            'cnp': forms.NumberInput(
                attrs={'class': 'form-control', 'placeholder': 'Introduceti Codul Numeric Personal'}),
            'numepacient': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Introduceti numele'}),
            'prenumepacient': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Introduceti prenumele'}),
            'adresa': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Introduceti adresa'}),
            'asigurare': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Asigurare'}),
        }
        labels = {
            'cnp': 'CNP',
            'numepacient': 'Nume',
            'prenumepacient': 'Prenume'
        }
        error_messages = {
            'cnp': {
                'unique': 'Acest CNP a mai fost folosit!'
            }
        }


class ConsultatieForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['data'].initial = datetime.datetime.today().strftime('%Y-%m-%d')

    class Meta:
        model = Consultatie
        fields = ['medicid', 'pacientid', 'medicamentid', 'data', 'diagnostic', 'dozamedicament']

        widgets = {
            'medicid': forms.Select(attrs={'class': 'custom-select'}),
            'pacientid': forms.Select(attrs={'class': 'custom-select'}),
            'medicamentid': forms.Select(attrs={'class': 'custom-select'}),
            'data': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Introduceti data'}),
            'diagnostic': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Introduceti diagnostic'}),
            'dozamedicament': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Introduceti doza'})
        }
        labels = {
            'medicid': 'Medic',
            'pacientid': 'Pacient',
            'medicamentid': 'Medicament',
            'data': 'Data',
            'diagnostic': 'Diagnostic',
            'dozamedicament': 'Doza medicament'
        }
        error_messages = {
            'data': {
                'invalid': 'Introduceti o data corespunzatoare (AAAA-LL-ZZ).'
            }
        }


class MedicamentForm(ModelForm):
    class Meta:
        model = Medicament
        fields = ('denumire',)
        widgets = {
            'denumire': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Introduceti denumirea'})
        }
        labels = {
            'denumire': 'Denumire'
        }


class SignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Parola'})
        self.fields['password2'].widget = forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Confirmarea parolei'})
        self.fields[
            'password1'].help_text = 'Parola nu poate fi asemanatoare cu username-ul.\nTrebuie sa contina cel putin 8 caractere.\nNu poate fi o parola deseori folosita.\nNu poate fi alcatuita doar din numere.'
        self.fields['password2'].help_text = 'Intordu din nou parola pentru verificare'

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Introduceti username-ul'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Prenume'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nume'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Adresa de e-mail'}),
        }
        labels = {
            'username': 'Username',
            'first_name': 'Nume',
            'last_name': 'Prenume',
            'email': 'Email',
        }
        help_texts = {
            'username': 'Obligatoriu. 150 de caractere sau mai putin. Doar litere, cifre si @/./+/-/_',
            'first_name': 'Optional',
            'last_name': 'Optional',
            'email': 'Optional',
        }
