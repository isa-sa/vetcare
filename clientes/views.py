from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Tutor
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