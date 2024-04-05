from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, UserChangeForm
from django.core.exceptions import ValidationError
import re
from .models import User
from django.contrib.auth import get_user_model


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    middle_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    registration_number = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control", 'placeholder': '0000/T.0000'
            }
        )
    )

    def clean_registration_number(self):
        registration_number = self.cleaned_data['registration_number']
        pattern = re.compile(r'^\d{5}/T\.\d{4}$')  # Desired pattern: 0000/T.0000
        
        if not pattern.match(registration_number):
            raise ValidationError("Registration number must be in the format 0000/T.0000")

        return registration_number

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        ),
        label="Password"
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        ),
        label="Confirm Password"
    )

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    gender = forms.ChoiceField(
        choices=[('M', 'Male'), ('F', 'Female')],
        widget=forms.Select(attrs={"class": "form-control"})
    )

    class Meta:
        model = User
        fields = ('first_name', 'middle_name', 'last_name', 'gender', 'registration_number', 'username', 'email', 'password1', 'password2')




class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'middle_name', 'registration_number')

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['email'].initial = user.email
            self.fields['first_name'].initial = user.first_name
            self.fields['last_name'].initial = user.last_name
            self.fields['middle_name'].initial = user.middle_name
            self.fields['registration_number'].initial = user.registration_number



    def clean_email(self):
        email = self.cleaned_data.get('email')
        if 'email' in self.changed_data and User.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError("This email address is already in use.")
        return email


class CustomPasswordChangeForm(PasswordChangeForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(user, *args, **kwargs)
        self.fields['old_password'].label = 'Old Password'
        self.fields['new_password1'].label = 'New Password'
        self.fields['new_password2'].label = 'Confirm New Password'


class ForgotPasswordForm(forms.Form):
    email = forms.EmailField(label='Email', max_length=254)

class ResetPasswordForm(forms.Form):
    password1 = forms.CharField(label='New password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm new password', widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match.")




class CustomUserCreationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'is_admin', 'is_cr', 'is_student', 'middle_name', 'registration_number', 'gender', 'groups', 'user_permissions')




class UpdateForm(UserChangeForm):
    # Define widgets for each field
    username = forms.TextInput(attrs={'class': 'form-control'})
    email = forms.EmailInput(attrs={'class': 'form-control'})
    first_name = forms.TextInput(attrs={'class': 'form-control'})
    middle_name = forms.TextInput(attrs={'class': 'form-control'})
    last_name = forms.TextInput(attrs={'class': 'form-control'})
    registration_number = forms.TextInput(attrs={'class': 'form-control'})
    gender = forms.Select(choices=[('M', 'Male'), ('F', 'Female')], attrs={'class': 'form-control'})


    class Meta:
        model = User
        fields = ('username', 'email', 'is_admin', 'is_cr', 'is_student', 'middle_name', 'registration_number', 'gender')