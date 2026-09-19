from django.db import models

<<<<<<< HEAD
class MensagemContato(models.Model):
    TIPO_CHOICES = [
        ('bug', 'Bug / Erro'),
        ('sugestao', 'Sugestão'),
        ('outros', 'Outros'),
    ]

    nome = models.CharField(max_length=100, verbose_name="Nome")
    email = models.EmailField(verbose_name="E-mail")
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES, default='sugestao', verbose_name="Tipo")
    mensagem = models.TextField(verbose_name="Mensagem")
    data_envio = models.DateTimeField(auto_now_add=True, verbose_name="Data de Envio")

    class Meta:
        verbose_name = "Mensagem de Contato"
        verbose_name_plural = "Mensagens de Contato"
        ordering = ['-data_envio']

    def __str__(self):
        return f"{self.nome} - {self.get_tipo_display()}"
