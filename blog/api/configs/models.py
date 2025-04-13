# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Artigos(models.Model):
    titulo = models.CharField(max_length=255)
    conteudo = models.TextField()
    slug = models.CharField(max_length=255)
    data_criacao = models.DateTimeField(auto_now_add=True)  # Alterado para DateTimeField
    publicado = models.BooleanField()

    class Meta:
        managed = False
        db_table = "artigos"

class Tag(models.Model):
    nome = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = "tag"

class ArtigoTag(models.Model):
    artigo = models.ForeignKey("Artigos", on_delete=models.CASCADE)
    tag = models.ForeignKey("Tag", on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = "artigo_tag"
