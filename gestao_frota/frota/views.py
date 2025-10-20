from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Carro

@login_required
def lista_carros(request):
    carros = Carro.objects.all().order_by('modelo')  # Ordena por modelo

    contexto = {'carros': carros}

    return render(request, 'frota/lista_carros.html', contexto)

@login_required
def adicionar_carro(request):
    if request.method == 'POST':
        # Pega os dados do formulário
        placa = request.POST.get('placa')
        marca = request.POST.get('marca')
        modelo = request.POST.get('modelo')
        ano = request.POST.get('ano')

        # Cria um novo objeto Carro e salva no banco
        Carro.objects.create(placa=placa, marca=marca, modelo=modelo, ano_fabricacao=ano)
        # Redireciona para a lista de carros após salvar
        return redirect('lista_carros')

    # Se o método não for POST, renderiza o formulário vazio
    return render(request, 'frota/form_carro.html')

@login_required
def editar_carro(request, pk):
    # Busca o carro específico pelo seu id (pk)
    carro = Carro.objects.get(id=pk)

    if request.method == 'POST':
        # Atualiza os campos do objeto 'carro' com os dados do formulário
        carro.placa = request.POST.get('placa')
        carro.marca = request.POST.get('marca')
        carro.modelo = request.POST.get('modelo')
        carro.ano_fabricacao = request.POST.get('ano')
        carro.em_manutencao = request.POST.get('em_manutencao') == 'on'  # Checkbox
        carro.save()  # Salva as alterações
        return redirect('lista_carros')
    else:
        contexto = {'carro': carro}
        return render(request, 'frota/form_carro_editar.html', contexto)

@login_required
def excluir_carro(request, pk):
    carro = Carro.objects.get(id=pk)
    if request.method == 'POST':
        carro.delete()
        return redirect('lista_carros')

    contexto = {'carro': carro}
    return render(request, 'frota/confirmar_exclusao.html', contexto)