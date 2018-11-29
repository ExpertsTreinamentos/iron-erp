from datetime import date, datetime

from django.db.utils import IntegrityError
from django.utils.timezone import get_default_timezone

import pytest
from freezegun import freeze_time

pytestmark = pytest.mark.django_db

from iron.core import api
from iron.core import models


def test_turma():
    with freeze_time(datetime(18,12,21,9,0,0,0,get_default_timezone())):
        curso = api.curso__cadastrar(nome='Curso', carga_horaria=20)
        prof = api.professor__cadastrar(nome='Professor')
        turma1 = api.turma__cadastrar(
            curso = curso,
            professor = prof,
            data_inicio = date(2019,1,7),
            vagas = 10,
        )
    
    with freeze_time(datetime(2019,1,7,0,0,0,0,get_default_timezone())):
        aluno1 = api.aluno__cadastrar(nome='Aluno 1')
        inscricao1 = api.inscricao__cadastrar(
            aluno = aluno1,
            turma = turma1,
        )
    assert inscricao1.observacao == models.Inscricao.REGULAR
    
    with freeze_time(datetime(2019,1,7,12,3,0,0,get_default_timezone())):
        data_hoje = datetime(2019,1,7,12,3,0,0,get_default_timezone()).date()
        turma2 = api.turma__cadastrar(
            curso = curso,
            professor = prof,
            data_inicio = date(2019,2,1),
            vagas = 10,
        )
        inscricao2 = api.inscricao__transferir(inscricao1, turma2, data_hoje)
    
    assert inscricao1.observacao == models.Inscricao.TRANSFERENCIA
    assert inscricao2.observacao == models.Inscricao.REGULAR
