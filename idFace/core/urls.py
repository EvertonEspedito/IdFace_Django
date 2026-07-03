from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import (
    dashboard,
    login,
    sair,
    cadastro_visitante,
    cadastro_aluno,
    cadastro_about
)

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('login/', login, name='login'),
    path('logout/', sair, name='logout'),
    path('cadastro-visitante/', cadastro_visitante, name='cadastro_visitante'),
    path('cadastro-aluno/', cadastro_aluno, name='cadastro_aluno'),
    path('cadastro-about/', cadastro_about, name='cadastro_about'),
]

urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)