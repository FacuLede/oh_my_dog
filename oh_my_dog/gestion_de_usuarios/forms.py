from user.models import User
from django.contrib.auth.forms import UserCreationForm

class UserUpdateForm(UserCreationForm) : 
    class Meta:
        model = User
        fields = ('username','email','dni')