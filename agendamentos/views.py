from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.core.exceptions import ValidationError
from .models import Consulta
from .forms import ConsultaForm
from .services import AgendamentoService

@login_required
def listar_agenda(request):
    consultas = Consulta.objects.select_related('pet', 'pet__tutor', 'veterinario').all()
    return render(request, 'agendamentos/lista.html', {'consultas': consultas})

@login_required
def novo_agendamento(request):
    if request.method == 'POST':
        form = ConsultaForm(request.POST)
        if form.is_valid():
            try:
                AgendamentoService.criar_agendamento(
                    pet=form.cleaned_data['pet'],
                    veterinario=form.cleaned_data['veterinario'],
                    data_hora=form.cleaned_data['data_hora'],
                    motivo=form.cleaned_data['motivo']
                )
                messages.success(request, 'Consulta agendada com sucesso!')
                return redirect('listar_agenda')
            except ValidationError as e:
                form.add_error(None, e.message)
    else:
        form = ConsultaForm()
    return render(request, 'agendamentos/form.html', {'form': form})

@login_required
@require_POST
def mudar_status_consulta(request, consulta_id):
    novo_status = request.POST.get('status')
    try:
        AgendamentoService.atualizar_status(consulta_id, novo_status)
        messages.success(request, 'Status da consulta atualizado.')
    except ValidationError as e:
        messages.error(request, e.message)
    return redirect('listar_agenda')