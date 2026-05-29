import cv2
import numpy as np

from deepface import DeepFace

from core.models import Pessoa
from core.models import Presenca

from django.utils import timezone
from datetime import timedelta

from reconhecimento.antispoofing import (
    AntiSpoofing
)

# ==========================
# ANTI-SPOOFING
# ==========================

antiSpoofing = AntiSpoofing()


def reconhecer():

    camera = cv2.VideoCapture(0)

    while True:

        conectado, frame = camera.read()

        if not conectado:
            break

        # ==========================
        # VERIFICAR PISCADA
        # ==========================

        real = antiSpoofing.verificarPiscada(
            frame
        )

        if not real:

            cv2.putText(
                frame,
                "Pisque para autenticar",
                (20, 100),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 0, 255),
                2
            )

            cv2.imshow(
                "Reconhecimento",
                frame
            )

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

            continue

        try:

            resultado = DeepFace.represent(
                img_path=frame,
                model_name='Facenet',
                enforce_detection=False
            )

            embeddingAtual = np.array(
                resultado[0]["embedding"]
            )

            pessoas = Pessoa.objects.exclude(
                embedding=None
            )

            for pessoa in pessoas:

                embeddingBanco = np.array(
                    pessoa.embedding
                )

                distancia = np.linalg.norm(
                    embeddingAtual - embeddingBanco
                )

                # ==========================
                # LIMIAR
                # ==========================

                if distancia < 10:

                    texto = (
                        f"{pessoa.nome} "
                        f"- {pessoa.cargo}"
                    )

                    cv2.putText(
                        frame,
                        texto,
                        (20, 50),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1,
                        (0, 255, 0),
                        2
                    )

                    # ==========================
                    # REGISTRO TEMPORAL
                    # ==========================

                    ultimaPresenca = (
                        Presenca.objects
                        .filter(pessoa=pessoa)
                        .order_by('-data_hora')
                        .first()
                    )

                    registrar = False

                    # Nunca registrou
                    if not ultimaPresenca:

                        registrar = True

                    else:

                        agora = timezone.now()

                        diferenca = (
                            agora -
                            ultimaPresenca.data_hora
                        )

                        # 5 minutos
                        if diferenca > timedelta(minutes=5):

                            registrar = True

                    # ==========================
                    # SALVAR PRESENÇA
                    # ==========================

                    if registrar:

                        Presenca.objects.create(
                            pessoa=pessoa
                        )

                        print(
                            f"Presença registrada:"
                            f" {pessoa.nome}"
                        )

                    break

        except Exception as erro:

            print(erro)

        cv2.imshow(
            "Reconhecimento",
            frame
        )

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    camera.release()
    cv2.destroyAllWindows()