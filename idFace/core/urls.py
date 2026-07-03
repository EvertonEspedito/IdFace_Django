from django.urls import path

from .views import(
dashboard,
 login,
 cadastro_visitante,
 cadastro_aluno,
 cadastro_about
)
urlpatterns = [

    path(
        '',
        dashboard,
        name='dashboard'
    ),
    path('login/', login, name='login'),
    path('cadastro-visitante/', cadastro_visitante, name='cadastro_visitante'),
    path('cadastro-aluno/', cadastro_aluno, name='cadastro_aluno'),
    path('cadastro-about/', cadastro_about, name='cadastro_about'),
]

