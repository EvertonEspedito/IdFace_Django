from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from deepface import DeepFace
from .models import (
    Pessoa,
    Presenca
)

from django.utils import timezone

@login_required(login_url='login')
def dashboard(request):

    hoje = timezone.now().date()

    totalPessoas = Pessoa.objects.count()

    presencasHoje = (
        Presenca.objects
        .filter(data_hora__date=hoje)
    )

    totalHoje = presencasHoje.count()

    ultimasPresencas = (
        Presenca.objects
        .select_related('pessoa')
        .order_by('-data_hora')[:10]
    )

    contexto = {

        'totalPessoas': totalPessoas,

        'totalHoje': totalHoje,

        'ultimasPresencas': ultimasPresencas
    }

    return render(
        request,
        'dashboard.html',
        contexto
    )

def login(request):

    if request.method == "POST":

        usuario = request.POST.get("username")
        senha = request.POST.get("password")

        user = authenticate(
            request,
            username=usuario,
            password=senha
        )

        if user is not None:

            auth_login(request, user)
            return redirect("dashboard")

        else:

            messages.error(
                request,
                "Usuário ou senha inválidos."
            )

    return render(
        request,
        "login.html"
    )

def sair(request):

    logout(request)

    return redirect("login")

def cadastro_visitante(request):
    return render(request, 'cadastro_visitante.html')

def cadastro_aluno(request):

    if request.method == "POST":

        matricula = request.POST.get("matricula")

        nome = request.POST.get("nome")

        sobrenome = request.POST.get("sobrenome")

        email = request.POST.get("email")

        foto = request.FILES.get("foto")

        novaPessoa = Pessoa.objects.create(

            nome=f"{nome} {sobrenome}",

            tipo="ALUNO",

            matricula=matricula,

            email=email,

            foto=foto

        )
        messages.success(
            request,
            "Aluno cadastrado com sucesso!"
        )
        try:

            resultado = DeepFace.represent(

                img_path=novaPessoa.foto.path,

                model_name="Facenet",

                enforce_detection=True

            )

            novaPessoa.embedding = resultado[0]["embedding"]

            novaPessoa.save()

        except Exception as erro:
                novaPessoa.delete()
                messages.error(request,"Não foi possível identificar um rosto na foto enviada.")

        return render(
            request,
            "cadastro_aluno.html"
        )

def cadastro_about(request):
    return render(request, 'cadastro_about.html')