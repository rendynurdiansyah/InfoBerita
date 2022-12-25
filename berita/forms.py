from dataclasses import fields
from django import forms
from django.db.models import fields
from django.forms import widgets
from .models import Artikel

class Artikelforms(forms.ModelForm):
    class Meta:
        model = Artikel
        fields = ('nama', 'judul', 'body', 'kategori')
        widgets = {
            "judul" : forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'type' :'text',
                    'placeholder':"judul berita",
                    'required':True
                }),
                
            "body" : forms.Textarea(
                attrs={
                    'class' : 'form-control',
                    'type' :'text',
                    'cols':'80',
                    'rows':'40',
                    'required':True
                }),
            "kategori" : forms.Select(
                attrs={
                    'class' : 'form-control',
                    'type' : 'text',
                    'required':True
                }),
        }
         