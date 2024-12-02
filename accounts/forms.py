from django  import forms
from .models import Profile
from django.core.validators import RegexValidator
from django.contrib.auth.hashers import make_password



class SignUp(forms.ModelForm):
    confirm_password = forms.CharField(
        max_length=128,
        widget=forms.PasswordInput(attrs={'class': 'form-control '}),
        label="Confirm Password"
    )
    class Meta:
        model = Profile
        fields = ['email', 'password']
        widgets = {
            'email' : forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }


    # def clean_password(self):
    #     password = self.cleaned_data.get('password')
    #     # Regex validation for password strength
    #     regex_validator = RegexValidator(
    #         regex=r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{4,10}$',
    #         message="Password must be 4 to 10 characters long and include at least one digit, one lowercase letter, and one uppercase letter."
    #     )
    #     regex_validator(password)
    #     return password

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")
        
        # Hash the password before saving to the database
        # cleaned_data['password'] = make_password(password)
        # return cleaned_data        
        