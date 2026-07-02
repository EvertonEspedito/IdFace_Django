import numpy as np

from core.models import Pessoa


LIMIAR = 0.75


def comparar(embedding):

    melhorPessoa = None

    menorDistancia = 999

    pessoas = Pessoa.objects.filter(
        ativo=True
    ).exclude(
        embedding=None
    )

    for pessoa in pessoas:

        distancia = np.linalg.norm(

            embedding -

            np.array(pessoa.embedding)

        )

        if distancia < menorDistancia:

            menorDistancia = distancia

            melhorPessoa = pessoa

    if menorDistancia < LIMIAR:

        return melhorPessoa, menorDistancia

    return None, menorDistancia