from django.db.models.signals import post_save
from django.dispatch import receiver
from deepface import DeepFace
from .models import Pessoa


@receiver(post_save, sender=Pessoa)
def gerar_embedding(sender, instance, created, **kwargs):

    if created and instance.foto:

        try:

            embedding = DeepFace.represent(
                img_path=instance.foto.path,
                model_name='Facenet',
                enforce_detection=False
            )

            instance.embedding = embedding[0]["embedding"]

            instance.save()

            print("Embedding gerado!")

        except Exception as erro:

            print("Erro:", erro)