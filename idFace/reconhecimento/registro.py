from datetime import timedelta

from django.utils import timezone

from core.models import Presenca


TEMPO_MINIMO = 5  # minutos


def registrar(pessoa, confianca):

    ultima = (
        Presenca.objects
        .filter(pessoa=pessoa)
        .order_by("-data_hora")
        .first()
    )

    agora = timezone.now()

    if ultima:

        diferenca = agora - ultima.data_hora

        if diferenca < timedelta(minutes=TEMPO_MINIMO):
            return False

    Presenca.objects.create(

        pessoa=pessoa,

        confianca=confianca,

        camera="Entrada Principal"

    )

    return True