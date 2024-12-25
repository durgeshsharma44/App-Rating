from django import forms
from .models import User, App

# User Login Form
class UserLoginForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={'placeholder': 'Username'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'})
    )

# Admin Login Form (Email-based)
class AdminLoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Email'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'})
    )

# User Registration Form (with Password Confirmation)
class RegistrationForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'})
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'})
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    # Validate Passwords Match
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            self.add_error('confirm_password', "Passwords do not match.")
        
        return cleaned_data
    
class AppForm(forms.ModelForm):
    class Meta:
        model = App
        # fields = ['name', 'url', 'category', 'sub_category', 'image']
        fields = ['app_name', 'app_link', 'category', 'sub_category', 'app_image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'url': forms.URLInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'sub_category': forms.Select(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'})
        }

class ScreenshotUploadForm(forms.ModelForm):
    class Meta:
        model = App
        fields = ['screenshot']
        widgets = {
            'screenshot': forms.ClearableFileInput(attrs={'class': 'form-control'})
        }
