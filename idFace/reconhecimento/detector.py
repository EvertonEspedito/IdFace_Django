import numpy as np

from core.models import Pessoa


LIMIAR = 0.75


def comparar(embeddingAtual):

    pessoas = Pessoa.objects.filter(
        ativo=True
    ).exclude(
        embedding=None
    )

    melhorPessoa = None

    menorDistancia = 999

    for pessoa in pessoas:

        embeddingBanco = np.array(
            pessoa.embedding
        )

        distancia = np.linalg.norm(

            embeddingAtual -

            embeddingBanco

        )

        if distancia < menorDistancia:

            menorDistancia = distancia

            melhorPessoa = pessoa

    if menorDistancia < LIMIAR:

        confianca = max(
            0,
            100 - menorDistancia*100
        )

        return melhorPessoa, confianca

    return None, 0