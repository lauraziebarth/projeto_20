from django.http import HttpResponse
from django.views import View
from dispositivosmercos.forms import FormDispositivo
from dispositivosmercos.models import Dispositivos
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate
from dispositivosmercos.gateway import busca_dispositivos_nao_excluidos, busca_um_dispositivo, alterar_dispositivo, excluir_dispositivo, cria_novo_dispositivo


@login_required
class ListarDispositivos(View):
    def get(self, request):
        dispositivos = busca_dispositivos_nao_excluidos()
        return render(request, 'listar_dispositivos.html', {'dispositivos': dispositivos})


@login_required
@administrador_required
class CadastrarDispositivo(View):
    def get(self, request):
        form = FormDispositivo()
        return render(request, 'cadastrar_dispositivo.html', {'form': form})

    def post(self, request):
        form = FormDispositivo(request.POST)

        if not form.is_valid():
            return render(request, 'cadastrar_dispositivo.html', {'form': form})

        sistema_operacional = form.cleaned_data['sistema_operacional']
        nome = form.cleaned_data['nome']
        descricao = form.cleaned_data['descricao']
        numeromodelo = form.cleaned_data['numeromodelo']
        versao = form.cleaned_data['versao']

        cria_novo_dispositivo(sistema_operacional, nome, descricao, numeromodelo, versao)

        return redirect(reverse('listar_dispositivos'))


@login_required
@administrador_required
class AlterarDispositivo(View):
    def get(self, request, dispositivo_id=None):
        dispositivo = busca_um_dispositivo(dispositivo_id)
        form = FormDispositivo(initial={'id': dispositivo.id, 'nome': dispositivo.nome, 'descricao': dispositivo.descricao, 'numeromodelo': dispositivo.numeromodelo, 'versao': dispositivo.versao})
        return render(request, 'alterar_dispositivo.html', {'form': form, 'dispositivo_id': dispositivo_id})

    def post(self, request, dispositivo_id=None):
        form = FormDispositivo(request.POST)

        if not form.is_valid():
            return render(request, 'alterar_dispositivo.html', {'form': form, 'dispositivo_id': dispositivo_id})

        sistema_operacional = form.cleaned_data['sistema_operacional']
        nome = form.cleaned_data['nome']
        descricao = form.cleaned_data['descricao']
        numeromodelo = form.cleaned_data['numeromodelo']
        versao = form.cleaned_data['versao']

        alterar_dispositivo(dispositivo_id, sistema_operacional, nome, descricao, numeromodelo, versao)

        return redirect(reverse('listar_dispositivos'))


@login_required
@administrador_required
class ExcluirDispositivo(View):
    def get(self, dispositivo_id=None):
        excluir_dispositivo(dispositivo_id)
        return redirect(reverse('listar_dispositivos'))


@login_required
class EmprestarDispositivo(View):
    def get(self, request, dispositivo_id=None):
        dispositivo = busca_um_dispositivo(dispositivo_id)
        form = FormDispositivo(initial={'id': dispositivo.id, 'nome': dispositivo.nome, 'descricao': dispositivo.descricao, 'numeromodelo': dispositivo.numeromodelo, 'versao': dispositivo.versao})
        return render(request, 'emprestar_dispositivo.html', {'form': form, 'dispositivo_id': dispositivo_id})

    def post(self, request, dispositivo_id=None):
        form = FormDispositivo(request.POST)

        if not form.is_valid():
            return render(request, 'alterar_dispositivo.html', {'form': form, 'dispositivo_id': dispositivo_id})

        pass

       # AQUI TEMOS QUE COLOCAR O VINCULO ENTRE DEVICE E COLABORADOR


@login_required
class DevolverDispositivo(View):
    def get(self, request, dispositivo_id=None):
        dispositivo = busca_um_dispositivo(dispositivo_id)
        form = FormDispositivo(initial={'id': dispositivo.id, 'nome': dispositivo.nome, 'descricao': dispositivo.descricao, 'numeromodelo': dispositivo.numeromodelo, 'versao': dispositivo.versao})
        return render(request, 'emprestar_dispositivo.html', {'form': form, 'dispositivo_id': dispositivo_id})

    def post(self, request, dispositivo_id=None):
        form = FormDispositivo(request.POST)

        if not form.is_valid():
            return render(request, 'alterar_dispositivo.html', {'form': form, 'dispositivo_id': dispositivo_id})

        pass
       # AQUI TEMOS QUE COLOCAR O VINCULO ENTRE DEVICE E COLABORADOR