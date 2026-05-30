from django.urls import path

from .views import(
dashboard,
 login,
 cadastro,
 cadastro_aluno
)
urlpatterns = [

    path(
        '',
        dashboard,
        name='dashboard'
    ),
    path('login/', login, name='login'),
    path('cadastro/', cadastro, name='cadastro'),
    path('cadastro-aluno/', cadastro_aluno, name='cadastro_aluno'),
]