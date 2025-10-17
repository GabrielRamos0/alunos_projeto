from django.shortcuts import render
from .models import Aluno

def lista_alunos(request):
    alunos = Aluno.objects.all().order_by('nome')
    return render(request, 'lista.html', {'alunos': alunos})
