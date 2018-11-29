from datetime import date

import pytest

pytestmark = pytest.mark.django_db

from iron.core import models

def test_db():
    curso = models.Curso.objects.create(nome='Curso')
    assert curso.pk

def test_cadastros_basicos():
    curso = models.Curso.objects.create(nome='Curso')
    prof = models.Professor.objects.create(nome='Professor')
    turma = models.Turma.objects.create(
        curso = curso,
        professor = prof,
        data_inicio = date(2000,1,1),
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
