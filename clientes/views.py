from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.db.models import ProtectedError
from .models import Tutor, Pet
from .forms import TutorForm, PetForm


@login_required
def listar_clientes(request):
    tutores = Tutor.objects.prefetch_related('pets').all().order_by('nome')
    return render(request, 'clientes/lista.html', {'tutores': tutores})


@login_required
def cadastrar_tutor(request):
    if request.method == 'POST':
        form = TutorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tutor cadastrado com sucesso!')
            return redirect('listar_clientes')
    else:
        form = TutorForm()
    return render(request, 'clientes/form.html', {'form': form, 'titulo': 'Cadastrar Novo Tutor'})


@login_required
def editar_tutor(request, tutor_id):
    tutor = get_object_or_404(Tutor, id=tutor_id)
    if request.method == 'POST':
        form = TutorForm(request.POST, instance=tutor)
        if form.is_valid():
            form.save()
            messages.success(request, f'Dados do tutor "{tutor.nome}" atualizados com sucesso!')
            return redirect('listar_clientes')
    else:
        form = TutorForm(instance=tutor)
    return render(request, 'clientes/form.html', {'form': form, 'titulo': f'Editar Tutor: {tutor.nome}'})


@login_required
@require_POST
def excluir_tutor(request, tutor_id):
    tutor = get_object_or_404(Tutor, id=tutor_id)
    nome = tutor.nome
    try:
        tutor.delete()
        messages.success(request, f'Tutor "{nome}" excluído com sucesso!')
    except ProtectedError:
        messages.error(
            request,
            f'Integridade Protegida: Não é possível excluir o tutor "{nome}" pois ele possui pets cadastrados.'
        )
    return redirect('listar_clientes')


@login_required
def cadastrar_pet(request):
    if request.method == 'POST':
        form = PetForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Pet cadastrado com sucesso!')
            return redirect('listar_clientes')
    else:
        form = PetForm()
    return render(request, 'clientes/form.html', {'form': form, 'titulo': 'Cadastrar Novo Pet'})


@login_required
def editar_pet(request, pet_id):
    pet = get_object_or_404(Pet, id=pet_id)
    if request.method == 'POST':
        form = PetForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            messages.success(request, f'Dados do pet "{pet.nome}" atualizados com sucesso!')
            return redirect('listar_clientes')
    else:
        form = PetForm(instance=pet)
    return render(request, 'clientes/form.html', {'form': form, 'titulo': f'Editar Pet: {pet.nome}'})


@login_required
@require_POST
def excluir_pet(request, pet_id):
    pet = get_object_or_404(Pet, id=pet_id)
    nome = pet.nome
    try:
        pet.delete()
        messages.success(request, f'Pet "{nome}" excluído com sucesso!')
    except ProtectedError:
        messages.error(
            request,
            f'Integridade Protegida: Não é possível excluir o pet "{nome}" pois existem consultas vinculadas a ele.'
        )
    return redirect('listar_clientes')