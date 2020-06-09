from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile,Project,UsabilityRating,DesignRating,ContentRating

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        
class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude =['posted_on','profile','user','rating',]

class DesignForm(forms.ModelForm):
    class Meta:
        model = DesignRating
        fields = ['rating', ]

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

class ContentForm(forms.ModelForm):
    class Meta:
        model = ContentRating
        fields = ['rating',]

class UsabilityForm(forms.ModelForm):
    class Meta:
        model = UsabilityRating
        fields = ['rating', ]

