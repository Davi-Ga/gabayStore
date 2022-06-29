from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Cloth
from django import forms

class RegisterUserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control form-control-lg'})
        self.fields['email'].widget.attrs.update({'class': 'form-control form-control-lg'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control form-control-lg'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control form-control-lg'})
    
    class Meta:
        model=User
        fields=['username','email','password1','password2']
        help_texts={
            'username':None,
            'password1':None,
            'password2':None,
        }
        
class ClothingForm(forms.ModelForm):
    class Meta:
        model=Cloth
        fields=['name','picture','size']
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'picture':forms.FileInput(attrs={'class':'form-control'}),
            'size':forms.Select(attrs={'class':'form-control'}),
        }