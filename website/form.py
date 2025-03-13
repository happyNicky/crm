from idlelib.tree import TreeItem

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.template.context_processors import request

from website.models import Record


class SingUpForm(UserCreationForm):
    email = forms.EmailField(label='',widget=forms.TextInput(attrs={
        'class':'form-control','placeholder':'Email Address'
    }))
    first_name =forms.CharField(max_length=30,widget=forms.TextInput(attrs={
        'class':'form-control','placeholder':'First Name'
    }))
    last_name = forms.CharField(max_length=30,widget=forms.TextInput(attrs={
        'class':'form-control','placeholder':'Last Name'
    }))
    class Meta:
        model=User
        fields=('username','email','first_name','last_name','password1','password2')

    def __init__(self, *args, **kwargs):
        super(SingUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields[
            'username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields[
            'password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields[
            'password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'

class AddRecordForm(forms.ModelForm):
    username=forms.CharField(label='',required=True,widget=forms.TextInput(attrs={
        'class':'form-control','placeholder':'username' }))
    email = forms.CharField(label='',required=True, widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'email'}))
    first_name = forms.CharField(label='',required=True, widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'first name'}))
    last_name = forms.CharField(label='',required=True, widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'last name'}))
    state = forms.CharField(label='',required=True, widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'state'}))
    address = forms.CharField(label='',required=True, widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'address'}))
    zip_code = forms.CharField(label='',required=True, widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'zip code'}))
    phone = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'phone'}),label='')
    city = forms.CharField(required=True,widget=forms.TextInput(attrs={
         'class':'form-control', 'placeholder':'city'}),label='')

    class Meta:
      model=Record
      exclude=('user',)




