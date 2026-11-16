from django.db import models

class Tutor(models.Model):
    nome = models.CharField(max_length=150)
    cpf = models.CharField(max_length=14, unique=True)
    telefone = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome} ({self.cpf})"


class Pet(models.Model):
    ESPECIES = [
        ('CAO', 'Cão'),
        ('GATO', 'Gato'),
        ('AVE', 'Ave'),
        ('OUTRO', 'Outro'),
    ]

    tutor = models.ForeignKey(Tutor, on_delete=models.PROTECT, related_name='pets')
    nome = models.CharField(max_length=100)
    especie = models.CharField(max_length=10, choices=ESPECIES)
    raca = models.CharField(max_length=100, blank=True)
    peso_kg = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    alergias = models.TextField(blank=True, help_text="Destacar alergias medicamentosas")

    def __str__(self):
        return f"{self.nome} - Tutor: {self.tutor.nome}"