from user.models import User
from django import forms 

class UserUpdateForm(forms.ModelForm) : 
    class Meta:
        model = User
        fields = ('username','email')
        exclude = ['password1','password2','dni']
