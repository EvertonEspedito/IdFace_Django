from django.db import models


class Pessoa(models.Model):

    CARGOS = [
        ("Aluno", "Aluno"),
        ("Professor", "Professor"),
        ("TAE", "TAE"),
        ("Diretor", "Diretor"),
        ("Gestor", "Gestor")
    ]

    matricula = models.CharField(
        max_length=20,
        unique=True
    )

    nome = models.CharField(
        max_length=100
    )

    cargo = models.CharField(
        max_length=20,
        choices=CARGOS
    )

    foto = models.ImageField(
        upload_to='rostos/'
    )
    
    # embedding facial
    embedding = models.JSONField(
        null=True,
        blank=True
    )

    criado_em = models.DateTimeField(
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

    def __str__(self):

        return f"{self.pessoa.nome} - {self.data_hora}"