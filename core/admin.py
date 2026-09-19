from django.contrib import admin
from .models import MensagemContato

@admin.register(MensagemContato)
class MensagemContatoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'tipo', 'data_envio')
    list_filter = ('tipo', 'data_envio')
    search_fields = ('nome', 'email', 'mensagem')
    readonly_fields = ('data_envio',)