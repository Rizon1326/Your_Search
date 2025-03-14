from django import forms
from django.core import validators

class TeachersRegistration(forms.Form):
    first_name=forms.CharField(max_length=50,label='Enter Your First Name',widget=forms.TextInput(attrs={'placeholder': 'Deepak'}) )
    last_name=forms.CharField(max_length=50,label='Enter Your Last Name',widget=forms.TextInput(attrs={'placeholder': 'Kumar'}) )
    email=forms.EmailField(max_length=50, label='Enter Your Email',widget=forms.EmailInput(attrs={'placeholder': 'abc@gmailcom'}) )
    password=forms.CharField(max_length=50, label='Enter Your Password',widget=forms.PasswordInput(attrs={'placeholder': '12334'}) )
    r_password=forms.CharField(max_length=50, label='Re-Enter Your Password',widget=forms.PasswordInput(attrs={'placeholder': '12334'}) )
    message=forms.CharField(widget=forms.Textarea,label='Enter Your Text')
    
    def clean(self):
        cleaned_data=super().clean()
        rightpass=self.cleaned_data['password']
        wrongpass=self.cleaned_data['r_password']
        if rightpass != wrongpass:
            raise forms.ValidationError('Password does not match')