import cv2


def iniciar_camera():

    camera = cv2.VideoCapture(0)

    if not camera.isOpened():
        raise Exception("Não foi possível abrir a câmera.")

    return camera