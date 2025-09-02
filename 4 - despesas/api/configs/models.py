# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class CategoriaDespesas(models.Model):
    tipo = models.CharField(unique=True, max_length=50)

    def __str__(self):
        return self.tipo
    
    class Meta:
        managed = False
        db_table = 'categoria_despesas'


class Despesa(models.Model):
    vencimento = models.DateField()
    descricao = models.CharField(max_length=50)
    montante = models.DecimalField(max_digits=10, decimal_places=2)
    tipo_despesas = models.ForeignKey(CategoriaDespesas, on_delete=models.CASCADE, related_name='despesas')
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='despesas')

    class Meta:
        managed = False
        db_table = 'despesa'


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('O email é obrigatório')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    objects = UserManager()
    
    class Meta:
        db_table = 'users'
