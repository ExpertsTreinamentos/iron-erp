from datetime import date

from django.db.utils import IntegrityError

import pytest

pytestmark = pytest.mark.django_db

from iron.core import models


def test_cadastros_basicos():
    curso = models.Curso.objects.create(nome='Curso', carga_horaria=20)
    prof = models.Professor.objects.create(nome='Professor')
    turma = models.Turma.objects.create(
        curso = curso,
        professor = prof,
        data_inicio = date(2000,1,1),
        vagas = 10,
    )
    aluno1 = models.Aluno.objects.create(nome='Aluno 1')
    inscricao1 = models.Inscricao.objects.create(
        turma = turma,
        aluno = aluno1,
    )
    aluno2 = models.Aluno.objects.create(nome='Aluno 2')
    inscricao2 = models.Inscricao.objects.create(
        turma = turma,
        aluno = aluno2,
    )
    # consultas
    assert turma == curso.turmas.all()[0]
    assert turma == prof.turmas.all()[0]
    assert turma.inscricoes.count() == 2
    assert turma == models.Turma.objects.filter(inscricoes__aluno=aluno1).get()

def test_cadastro_aluno():
    aluno1 = models.Aluno.objects.create(nome='Aluno 1')
    aluno2 = models.Aluno.objects.create(nome='Aluno 2')
    aluno3 = models.Aluno.objects.create(nome='Aluno 3', cpf='1234')
    with pytest.raises(IntegrityError):
        aluno4 = models.Aluno.objects.create(nome='Aluno 4', cpf='1234')
    
