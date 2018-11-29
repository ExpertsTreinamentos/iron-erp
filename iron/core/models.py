from django.db import models

# Create your models here.

class Curso(models.Model):
    nome = models.CharField(max_length=1024)
    
    def __str__(self):
        return self.nome


class Professor(models.Model):
    nome = models.CharField(max_length=1024)
    
    def __str__(self):
        return self.nome


class Turma(models.Model):
    curso = models.ForeignKey(Curso, related_name='turmas', on_delete='PROTECT')
    professor = models.ForeignKey(Professor, related_name='turmas', on_delete='PROTECT')
    data_inicio = models.DateField()
    
    def __str__(self):
        return f'{self.curso} com o professor {self.professor} iniciando em {self.data_inicio}'


class Aluno(models.Model):
    nome = models.CharField(max_length=1024)
    
    def __str__(self):
        return self.nome


class Inscricao(models.Model):
    turma = models.ForeignKey(Turma, related_name='inscricoes', on_delete='PROTECT')
    aluno = models.ForeignKey(Aluno, related_name='inscricoes', on_delete='PROTECT')
    
    def __str__(self):
        return f'{self.aluno} inscrito em {self.turma}'
