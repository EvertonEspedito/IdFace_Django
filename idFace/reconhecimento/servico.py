import numpy as np

from deepface import DeepFace

from .comparador import comparar
from .registro import registrar


class ServicoReconhecimento:

    def reconhecer(self, rosto):

        try:

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

            if pessoa:

                registrar(
                    pessoa,
                    confianca
                )

            return pessoa, confianca

        except Exception as erro:

            print(erro)

            return None, 0