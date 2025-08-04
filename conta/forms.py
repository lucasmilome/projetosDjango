from django import forms

class LoginForm(forms.Form):
    login = forms.CharField(
        label='Usuário',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex: mariaFernanda',
            }
        ),
    )
    password = forms.CharField(
        label='Senha',
        required=True,
        max_length=80,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Informe a sua senha',
            }
        ),
    )


class RegisterForm(forms.Form):
    login = forms.CharField(
        label='Usuário',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex: mariaFernanda'
            }
        ),
    )
    email = forms.EmailInput(
        label='E-mail',
        required=True,
        max_length = 100,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex: mariafernanda@gmail.com',
            }
        ),
    )
    password = forms.PasswordInput(
        label='Senha',
        required=True,
        max_length=80,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Informe a sua senha',
            }
        ),
    )
    reenter_password = forms.PasswordInput(
        label='Confirme a senha',
        required=True,
        max_length=80,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Informe a senha novamente',
            }
        ),
    )
