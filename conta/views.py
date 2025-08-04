from django.shortcuts import render, redirect
from conta.forms import LoginForm, RegisterForm

# Create your views here.
def login(request):
    form = LoginForm()
    return render(request, 'conta/login.html', {'form': form})

def register(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form['login'].value() == '' or form['email'].value() == None:
            return redirect('register')
        
        if form['password'].value() != form['reenter_password']:
            return redirect('register')
        
    return render(request, 'conta/register.html', {'form': form})