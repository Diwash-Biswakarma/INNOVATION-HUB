from django import forms
from .models import Work


class WorkForm(forms.ModelForm):
    class Meta:
        model = Work
        fields = '__all__'


class Blogform(forms.ModelForm):
    class Meta:
        fields = ['blog_name', 'blog','blog_writer']


class Messageform(forms.ModelForm):
    class Meta:
        fields = ['full_name', 'email', 'message']
