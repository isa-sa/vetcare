from django.db import transaction
from django.core.exceptions import ValidationError
from .models import Consulta

class AgendamentoService:
    @staticmethod
    @transaction.atomic
    def criar_agendamento(pet, veterinario, data_hora, motivo):
        # Regra de Negócio: Impedir choque de horário para o mesmo veterinário
        conflito = Consulta.objects.filter(
            veterinario=veterinario,
            data_hora=data_hora
        ).exclude(status='CANCELADA').exists()

        if conflito:
            raise ValidationError("Este veterinário já possui uma consulta ativa neste horário.")

        consulta = Consulta.objects.create(
            pet=pet,
            veterinario=veterinario,
            data_hora=data_hora,
            motivo=motivo,
            status='AGENDADA'
        )
        return consulta

    @staticmethod
    @transaction.atomic
    def atualizar_status(consulta_id, novo_status):
        consulta = Consulta.objects.select_for_update().get(id=consulta_id)
        if consulta.status == 'CONCLUIDA':
            raise ValidationError("Não é possível alterar uma consulta já concluída.")
        consulta.status = novo_status
        consulta.save()
        return consulta