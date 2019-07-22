from django.views import View
from colaboradoresmercos.forms import FormColaborador, FormLogin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse


class CadastrarColaborador(View):
    def get(self, request):
        form = FormColaborador()
        return render(request, 'cadastrar_colaborador.html', {'form': form})

    def post(self, request):
        from core.colaborador import cria_novo_colaborador

        form = FormColaborador(request.POST)

        if not form.is_valid():
            return render(request, 'cadastrar_colaborador.html', {'form': form})

        nome = form.cleaned_data['nome']
        email = form.cleaned_data['email']
        area = form.cleaned_data['area']
        senha = form.cleaned_data['senha']

        user = User.objects.create(first_name=name, username=email, email=email)
        user.set_password(senha)
        user.save()

        cria_novo_colaborador(user.id, nome, email, area)

        return redirect(reverse('login'))


class Login(View):
    def get(self, request):
        form = FormLogin()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = FormColaborador(request.POST)

        if not form.is_valid():
            return render(request, 'login.html', {'form': form})

    pass
