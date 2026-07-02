from django.db import models


from django.db import models


class Pessoa(models.Model):

    TIPOS = [
        ('ALUNO', 'Aluno'),
        ('VISITANTE', 'Visitante'),
    ]

    nome = models.CharField(
        max_length=200
    )

    tipo = models.CharField(
        max_length=20,
        choices=TIPOS
    )

    matricula = models.CharField(
        max_length=30,
        blank=True,
        null=True
    )

    cpf = models.CharField(
        max_length=14,
        blank=True,
        null=True
    )

    email = models.EmailField(
        blank=True,
        null=True
    )

    empresa = models.CharField(
        max_length=150,
        blank=True,
        null=True
    )

    motivo_visita = models.CharField(
        max_length=200,
        blank=True,
        null=True
    )

    foto = models.ImageField(
        upload_to="rostos/"
    )

    embedding = models.JSONField(
        blank=True,
        null=True
    )

    ativo = models.BooleanField(
        default=True
    )

    data_cadastro = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.nome
    
class Presenca(models.Model):

    pessoa = models.ForeignKey(
        Pessoa,
        on_delete=models.CASCADE
    )

    data_hora = models.DateTimeField(
        auto_now_add=True
    )

    camera = models.CharField(
        max_length=100,
        default="Entrada Principal"
    )

    confianca = models.FloatField(
        default=0
    )

    def __str__(self):

        return f"{self.pessoa.nome} - {self.data_hora}"