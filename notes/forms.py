from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Note

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=255, help_text="Required.")

    class Meta:
        model=User
        fields=('username', 'email', 'password1', 'password2')


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'memo', 'important']
        
