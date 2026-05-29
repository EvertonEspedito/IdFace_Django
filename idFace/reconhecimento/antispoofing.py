import cv2
import mediapipe as mp
import numpy as np

from scipy.spatial import distance


mp_face_mesh = mp.solutions.face_mesh


class AntiSpoofing:

    def __init__(self):

        self.face_mesh = (
            mp_face_mesh.FaceMesh(
                max_num_faces=1,
                refine_landmarks=True
            )
        )

        self.EAR_LIMIAR = 0.20

    # ==========================
    # DISTÂNCIA ENTRE PONTOS
    # ==========================

    def calcularEAR(self, olho):

        A = distance.euclidean(
            olho[1],
            olho[5]
        )

        B = distance.euclidean(
            olho[2],
            olho[4]
        )

        C = distance.euclidean(
            olho[0],
            olho[3]
        )

        ear = (A + B) / (2.0 * C)

        return ear

    # ==========================
    # DETECTAR PISCADA
    # ==========================

    def verificarPiscada(self, frame):

        rgb = cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2RGB
        )

        resultado = self.face_mesh.process(rgb)

        if not resultado.multi_face_landmarks:

            return False

        face = resultado.multi_face_landmarks[0]

        h, w, _ = frame.shape

        # ==========================
        # PONTOS DOS OLHOS
        # ==========================

        olho_esquerdo_ids = [
            33, 160, 158, 133, 153, 144
        ]

        olho_direito_ids = [
            362, 385, 387, 263, 373, 380
        ]

        olho_esquerdo = []
        olho_direito = []

        for idx in olho_esquerdo_ids:

            ponto = face.landmark[idx]

            x = int(ponto.x * w)
            y = int(ponto.y * h)

            olho_esquerdo.append((x, y))

        for idx in olho_direito_ids:

            ponto = face.landmark[idx]

            x = int(ponto.x * w)
            y = int(ponto.y * h)

            olho_direito.append((x, y))

        ear_esquerdo = self.calcularEAR(
            olho_esquerdo
        )

        ear_direito = self.calcularEAR(
            olho_direito
        )

        ear = (
            ear_esquerdo +
            ear_direito
        ) / 2

        # ==========================
        # PISCADA
        # ==========================

        if ear < self.EAR_LIMIAR:

            return True

        return False