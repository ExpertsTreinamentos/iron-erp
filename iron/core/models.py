from django.db import models
from django.utils import timezone

# Create your models here.

class Curso(models.Model):
    REGULAR = 'REG'
    IN_COMPANY = 'INCOMP'
    TIPO = (
        (REGULAR, 'Regular'),
        (IN_COMPANY, 'In-company'),
    )
    
    nome = models.CharField(max_length=1024)
    tipo = models.CharField(max_length=16, choices=TIPO, default=REGULAR)
    carga_horaria = models.PositiveIntegerField()
    
    def __str__(self):
        return self.nome


class Professor(models.Model):
    nome = models.CharField(max_length=1024)
    
    def __str__(self):
        return self.nome


class Turma(models.Model):
    curso = models.ForeignKey(Curso, related_name='turmas', on_delete='PROTECT')
    professor = models.ForeignKey(Professor, related_name='turmas', on_delete='PROTECT')
    vagas = models.PositiveIntegerField()
    data_inicio = models.DateField()
    data_encerramento = models.DateField(null=True, blank=True)
    datahora_fechamento_inscricao = models.DateTimeField(null=True, blank=True) # flag de abretura/fechamento
    observacao = models.TextField(blank=True)
    
    def __str__(self):
        return f'{self.curso} com o professor {self.professor} iniciando em {self.data_inicio}'


class Aluno(models.Model):
    nome = models.CharField(max_length=1024)
    cpf = models.CharField(max_length=11, unique=True, null=True, blank=True)
    
    def __str__(self):
        return self.nome


class Inscricao(models.Model):
    REGULAR = 'REG'
    TRANSFERENCIA = 'TRANS'
    CANCELAMENTO = 'CANC'
    REPOSICAO = 'REP'
    OBS = (
        (REGULAR, 'Regular'),
        (TRANSFERENCIA, 'Transferência'),
        (CANCELAMENTO, 'Cancelamento'),
        (REPOSICAO, 'Reposição'),
    )
    
    aluno = models.ForeignKey(Aluno, related_name='inscricoes', on_delete='PROTECT')
    turma = models.ForeignKey(Turma, related_name='inscricoes', on_delete='PROTECT')
    data_entrada = models.DateField(default=timezone.now)
    data_saida = models.DateField(null=True, blank=True)
    observacao = models.CharField(max_length=16, choices=OBS, default=REGULAR)
    
    def __str__(self):
        return f'{self.aluno} inscrito em {self.turma}'
