from django.db import transaction
from django.utils import timezone

from . import models


def curso__cadastrar(nome, carga_horaria):
    return models.Curso.objects.create(nome=nome, carga_horaria=carga_horaria)

def professor__cadastrar(nome):
    return models.Professor.objects.create(nome=nome)

def turma__cadastrar(curso, professor, data_inicio, vagas):
    return models.Turma.objects.create(
        curso = curso,
        professor = professor,
        data_inicio = data_inicio,
        vagas = vagas,
    )

def aluno__cadastrar(nome, cpf=None):
    return models.Aluno.objects.create(nome=nome, cpf=cpf)

def inscricao__cadastrar(aluno, turma):
    return models.Inscricao.objects.create(
        aluno = aluno,
        turma = turma,
    )

@transaction.atomic
def inscricao__transferir(inscricao_atual, turma_destino, data_saida):
    inscricao_atual.observacao = models.Inscricao.TRANSFERENCIA
    inscricao_atual.data_saida = data_saida
    inscricao_atual.save()
    inscricao_nova = inscricao__cadastrar(
        aluno = inscricao_atual.aluno,
        turma = turma_destino,
    )
    return inscricao_nova
