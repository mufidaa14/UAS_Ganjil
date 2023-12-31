from django.forms import ModelForm
from django import forms
from .models import absen

class Formabsen(ModelForm):
    class Meta:
        model = absen
        fields = '__all__'

        widgets = {
            'hari' : forms.TextInput({'class' : 'form-control'}),
            'makul' : forms.TextInput({'class' : 'form-control'}),
            'nama' : forms.TextInput({'class' : 'form-control'}),
            'npm' : forms.TextInput({'class' : 'form-control'}),
            'prodi' : forms.TextInput({'class' : 'form-control'}),
            'fakultas' : forms.TextInput({'class' : 'form-control'}),
            'keterangan' : forms.TextInput({'class' : 'form-control'}),
        }

        