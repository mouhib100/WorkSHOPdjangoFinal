from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class RegisterForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['cin', 'first_name', 'last_name', 'email', 'username', 'password1', 'password2']
    def save(self, commit: True) -> Any:
        return super(RegisterForm, self).save(commit)  