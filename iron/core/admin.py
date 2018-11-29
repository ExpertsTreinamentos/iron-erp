from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Curso)
admin.site.register(Professor)
admin.site.register(Turma)
admin.site.register(Aluno)
admin.site.register(Inscricao)
