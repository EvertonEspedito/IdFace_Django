import cv2
import numpy as np

from deepface import DeepFace
import time
from .camera import iniciar_camera
from .detector import detectar
from .comparador import comparar
from .registro import registrar


def reconhecer():

    camera = iniciar_camera()

    ultimoReconhecimento = 0

    ultimaPessoa = None

    ultimaConfianca = 0

    TEMPO_CACHE = 2

    while True:

        conectado, frame = camera.read()

        if not conectado:
            break

        # Detecta os rostos
        faces, cinza = detectar(frame)
        agora = time.time()

        for (x, y, w, h) in faces:

            # Adiciona uma pequena margem ao redor do rosto
            margem = 20

            x1 = max(0, x - margem)
            y1 = max(0, y - margem)

            x2 = min(frame.shape[1], x + w + margem)
            y2 = min(frame.shape[0], y + h + margem)

            rosto = frame[y1:y2, x1:x2]

            try:

                # Gera o embedding do rosto
                if agora - ultimoReconhecimento > TEMPO_CACHE:

                    resultado = DeepFace.represent(
                        img_path=rosto,
                        model_name="Facenet",
                        enforce_detection=False
                    )

                    embedding = np.array(
                        resultado[0]["embedding"]
                    )

                    pessoa, confianca = comparar(
                        embedding
                    )

                    ultimoReconhecimento = agora

                    ultimaPessoa = pessoa

                    ultimaConfianca = confianca

                else:

                    pessoa = ultimaPessoa

                    confianca = ultimaConfianca

                embedding = np.array(
                    resultado[0]["embedding"]
                )

                # Procura a pessoa no banco
                pessoa, confianca = comparar(
                    embedding
                )

                if pessoa:

                    texto = (
                        f"{pessoa.nome} "
                        f"({confianca:.1f}%)"
                    )

                    cor = (0, 255, 0)

                    registrou = registrar(
                        pessoa,
                        confianca
                    )

                    if registrou:
                        print(f"{pessoa.nome} entrou na instituição.")

                else:

                    texto = "Desconhecido"

                    cor = (0, 0, 255)

            except Exception as erro:

                print("Erro:", erro)

                texto = "Erro"

                cor = (0, 0, 255)

            # Desenha o retângulo
            cv2.rectangle(
                frame,
                (x, y),
                (x + w, y + h),
                cor,
                2
            )

            # Escreve o nome
            cv2.putText(
                frame,
                texto,
                (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                cor,
                2
            )

        cv2.imshow(
            "SIRA - Reconhecimento Facial",
            frame
        )

        tecla = cv2.waitKey(1) & 0xFF

        if tecla == ord("q"):
            break

    camera.release()

    cv2.destroyAllWindows()