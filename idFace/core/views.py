from django.shortcuts import render

from .models import (
    Pessoa,
    Presenca
)

from django.utils import timezone


def dashboard(request):

    hoje = timezone.now().date()

    totalPessoas = Pessoa.objects.count()

    presencasHoje = (
        Presenca.objects
        .filter(data_hora__date=hoje)
    )

    totalHoje = presencasHoje.count()

    ultimasPresencas = (
        Presenca.objects
        .select_related('pessoa')
        .order_by('-data_hora')[:10]
    )

    contexto = {

        'totalPessoas': totalPessoas,

        'totalHoje': totalHoje,

        'ultimasPresencas': ultimasPresencas
    }

    return render(
        request,
        'dashboard.html',
        contexto
    )