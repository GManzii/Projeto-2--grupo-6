from django.db import models

# Create your models here.
# formulario de contato
class MensagemContato(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    mensagem = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome} - {self.email}"

# 1. Perfil da Empresa
class Empresa(models.Model):
    nome = models.CharField(max_length=100)
    setor = models.CharField(max_length=50)
    porte = models.CharField(max_length=20)

    def __str__(self):
        return self.nome

# 2. Questionario ESG (Perguntas)
class PerguntaESG(models.Model):
    enunciado = models.CharField(max_length=255)
    categoria = models.CharField(max_length=20) # Ambiental, Social, Governança

    def __str__(self):
        return self.enunciado

# 3. Lista de Praticas ESG
class PraticaESG(models.Model):
    titulo = models.CharField(max_length=100)
    categoria = models.CharField(max_length=20)
    descricao = models.TextField()

    def __str__(self):
        return self.titulo
