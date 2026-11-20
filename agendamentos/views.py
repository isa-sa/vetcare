from datetime import datetime, timedelta
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.utils import timezone
from .models import Consulta
from .forms import ConsultaForm
from .services import AgendamentoService


@login_required
def listar_agenda(request):
    data_str = request.GET.get('data')
    try:
        data_selecionada = datetime.strptime(data_str, '%Y-%m-%d').date() if data_str else timezone.localdate()
    except ValueError:
        data_selecionada = timezone.localdate()

    dia_anterior = data_selecionada - timedelta(days=1)
    proximo_dia = data_selecionada + timedelta(days=1)

    consultas_dia = Consulta.objects.select_related('pet', 'pet__tutor', 'veterinario').filter(
        data_hora__date=data_selecionada
    )

    grade_horarios = []
    horas_padrao = range(8, 19)

    for hora in horas_padrao:
        horario_label = f"{hora:02d}:00"
        data_hora_iso = f"{data_selecionada.strftime('%Y-%m-%d')}T{horario_label}"
        consultas_no_horario = []

        for c in consultas_dia:
            dt_local = timezone.localtime(c.data_hora) if timezone.is_aware(c.data_hora) else c.data_hora
            if dt_local.hour == hora:
                consultas_no_horario.append(c)

        grade_horarios.append({
            'horario': horario_label,
            'data_hora_iso': data_hora_iso,
            'consultas': consultas_no_horario,
        })

    consultas_fora_grade = [
        c for c in consultas_dia
        if (timezone.localtime(c.data_hora) if timezone.is_aware(c.data_hora) else c.data_hora).hour not in horas_padrao
    ]

    contexto = {
        'data_selecionada': data_selecionada,
        'hoje': timezone.localdate(),
        'dia_anterior': dia_anterior.strftime('%Y-%m-%d'),
        'proximo_dia': proximo_dia.strftime('%Y-%m-%d'),
        'grade_horarios': grade_horarios,
        'consultas_fora_grade': consultas_fora_grade,
    }
    return render(request, 'agendamentos/lista.html', contexto)


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
                data_url = form.cleaned_data['data_hora'].strftime('%Y-%m-%d')
                return redirect(f"/agendamentos/?data={data_url}")
            except ValidationError as e:
                form.add_error(None, e.message)
    else:
        initial_data = {}
        data_hora_param = request.GET.get('data_hora')
        if data_hora_param:
            initial_data['data_hora'] = data_hora_param
        form = ConsultaForm(initial=initial_data)

    return render(request, 'agendamentos/form.html', {'form': form})


@login_required
@require_POST
def mudar_status_consulta(request, consulta_id):
    novo_status = request.POST.get('status')
    data_retorno = request.POST.get('data_retorno', '')
    try:
        AgendamentoService.atualizar_status(consulta_id, novo_status)
        messages.success(request, 'Status da consulta atualizado.')
    except ValidationError as e:
        messages.error(request, e.message)

    if data_retorno:
        return redirect(f"/agendamentos/?data={data_retorno}")
    return redirect('listar_agenda')