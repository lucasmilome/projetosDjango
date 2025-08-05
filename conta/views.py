from django.shortcuts import render, redirect
from conta.forms import LoginForm, RegisterForm
from django.contrib.auth.models import User

# Create your views here.
def login(request):
    form = LoginForm()
    return render(request, 'conta/login.html', {'form': form})

def register(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            nome_usuario = form['login'].value().strip()
            email_usuario = form['email'].value().strip()
            senha = form['password'].value().strip()
            confirma_senha = form['reenter_password'].value().strip()

            if nome_usuario == '' or email_usuario == '' or senha == '' or confirma_senha == '':
                return redirect('register')
            
            if senha != confirma_senha:
                return redirect('register')
            
            user_exists = User.objects.filter(username=nome_usuario).exists()
            email_exists = User.objects.filter(email=email_usuario).exists()

            if user_exists:
                return redirect('register')
            
            if email_exists:
                return redirect('register')

            new_user = User.objects.create_user(
                username=nome_usuario,
                email=email_usuario,
                password=senha,
            )

            new_user.save()
            return redirect('login')
        
    return render(request, 'conta/register.html', {'form': form})