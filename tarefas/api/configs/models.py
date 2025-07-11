from django.db import models


class Usuario(models.Model):
    username = models.CharField(unique=True, max_length=50)
    email = models.CharField(unique=True, max_length=100)
    senha_hash = models.TextField()
    data_criacao = models.DateField(auto_now_add=True)

    class Meta:
        db_table = "usuario"
        managed = False

class Tarefa(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    data_criacao = models.DateTimeField(blank=True, null=True)
    prazo = models.DateTimeField(blank=True, null=True)
    concluida = models.BooleanField(blank=True, null=True)
    prioridade = models.CharField(max_length=20, blank=True, null=True)
    categoria = models.CharField(max_length=50, blank=True, null=True)
    usuario = models.ForeignKey("Usuario", on_delete=models.CASCADE)

    class Meta:
        db_table = "tarefa"
        managed = False