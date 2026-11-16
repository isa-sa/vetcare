from django.db import models
from django.contrib.auth.models import User
from clientes.models import Pet

class Consulta(models.Model):
    STATUS_CHOICES = [
        ('AGENDADA', 'Agendada'),
        ('EM_ATENDIMENTO', 'Em Atendimento'),
        ('CONCLUIDA', 'Concluída'),
        ('CANCELADA', 'Cancelada'),
    ]

    pet = models.ForeignKey(Pet, on_delete=models.PROTECT, related_name='consultas')
    veterinario = models.ForeignKey(User, on_delete=models.PROTECT, related_name='agenda_vet')
    data_hora = models.DateTimeField()
    motivo = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='AGENDADA')
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['data_hora']
        constraints = [
            models.UniqueConstraint(
                fields=['veterinario', 'data_hora'],
                condition=~models.Q(status='CANCELADA'),
                name='unique_horario_veterinario_ativo'
            )
        ]

    def __str__(self):
        return f"{self.data_hora.strftime('%d/%m %H:%M')} - {self.pet.nome}"