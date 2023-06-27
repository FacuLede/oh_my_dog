from user.models import User
from django import forms 

class UserUpdateForm(forms.ModelForm) : 
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email')
        exclude = ['password1','password2','dni']

