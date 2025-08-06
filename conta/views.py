from django.shortcuts import render, redirect
from conta.forms import LoginForm, RegisterForm
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages


# Create your views here.
def login(request):
    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            nome_usuario = form["login"].value().strip()
            senha = form["password"].value().strip()

            if nome_usuario == "" or senha == "":
                messages.error(request, "Todos os campos são obrigatórios!")
                return render(request, "conta/login.html", {"form": form})

            credenciais_usuario = auth.authenticate(
                request,
                username=nome_usuario,
                password=senha,
            )

            if credenciais_usuario == None:
                messages.error(request, "Login falho! Tente novamente")
                return render(request, "conta/login.html", {"form": form})

            auth.login(request, credenciais_usuario)
            return redirect("projeto_index")

    return render(request, "conta/login.html", {"form": form})


def register(request):
    form = RegisterForm()

    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            nome_usuario = form["login"].value().strip()
            email_usuario = form["email"].value().strip()
            senha = form["password"].value().strip()
            confirma_senha = form["reenter_password"].value().strip()

            if (
                nome_usuario == ""
                or email_usuario == ""
                or senha == ""
                or confirma_senha == ""
            ):
                return redirect("register")

            if senha != confirma_senha:
                messages.error(request, "As senhas não coincidem!")
                return render(request, "conta/register.html", {"form": form})

            user_exists = User.objects.filter(username=nome_usuario).exists()
            email_exists = User.objects.filter(email=email_usuario).exists()

            if user_exists:
                messages.error(request, "Já existe um usúario com este nome")
                return render(request, "conta/register.html", {"form": form})

            if email_exists:
                messages.error(request, "Esse e-mail já está cadastrado!")
                return render(request, "conta/register.html", {"form": form})

            new_user = User.objects.create_user(
                username=nome_usuario,
                email=email_usuario,
                password=senha,
            )

            new_user.save()

            messages.success(request, "Usuário cadastrado com sucesso!")

    return render(request, "conta/register.html", {"form": form})
