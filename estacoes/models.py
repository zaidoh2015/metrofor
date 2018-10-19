from django.db import models
from django.contrib.auth.models import User

from gates.models import Gate, GATES_CHOICES

ESTACOES_CHOICES = (
    ('CHI', '1 - Chico da Silva'),
    ('JAL', '2 - José de Alencar'),
    ('SBE', '3 - São Benedito'),
    ('BEN', '4 - Benfica'),
    ('PCI', '5 - Padre Cícero'),
    ('POR', '6 - Porangabussu'),
    ('COU', '7 - Couto Fernandes'),
    ('JUK', '8 - Juscelino Kubsheck'),
    ('PAR', '9 - Parangaba'),
    ('VIP', '10 - Vila Pery'),
    ('SAT', '11 - Manoel Sátiro'),
    ('MON', '12 - Mondubim'),
    ('ESP', '13 - Esperança'),
    ('ARA', '14 - Aracapé'),
    ('ALT', '15 - Alto Alegre'),
    ('RAQ', '16 - Raquel de Queiróz'),
    ('VIT', '17 - Virgílio Távora'),
    ('MAR', '18 - Maracanaú'),
    ('JER', '19 - Jereissati'),
    ('CAB', '20 - Carlito Benevides'),
)


class Estacao(models.Model):
    nome = models.TextField(choices=ESTACOES_CHOICES)
    gates = models.ManyToManyField(Gate)
    observacao = models.TextField(null=True, blank=True)
    agente_abre = models.ForeignKey(User, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return "Nome: {0}".format(self.nome)


